import httpx
import pygame
import settings
import space_game_entities
import space_game_ui
import space_game_utils
from space_game_entities import Player, projectiles, Asteroid, asteroids
from space_game_utils import load_background, get_device_id, ApiClient, draw_hud
from space_game_ui import Menu

# Grundlegendes Setup
pygame.init()

# Mixer initialisieren (Menu spielt bereits eigene Sounds, Player einen Schuss-Sound)
pygame.mixer.init()

# space-game-entities, space-game-ui und space-game-utils mitteilen, wo die Assets liegen
space_game_entities.configure(settings.ASSETS_PATH)
space_game_ui.configure(settings.ASSETS_PATH)
space_game_utils.configure(settings.ASSETS_PATH)

# Fenster erstellen
display_surface = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
)

# Fenstertitel setzen
pygame.display.set_caption("Space Shooter")

# Clock definieren
clock = pygame.time.Clock()
delta_time = 0

# Hintergrund laden (auch als Kulisse für den Startbildschirm)
background = load_background(
    settings.ASSETS_PATH / "images" / "background" / "starfield" / "tile_1.png"
)

# Menu vorbereiten
menu = Menu(display_surface)

# Startbildschirm anzeigen und Namen abfragen
player_name = menu.start_screen(background=background)

if player_name is None:
    pygame.quit()
    raise SystemExit

# Sounds laden
game_music = pygame.mixer.Sound(
    settings.ASSETS_PATH / "music" / "synthwave" / "loop_7.mp3"
)
GAME_MUSIC_VOLUME = 0.5
game_music.set_volume(GAME_MUSIC_VOLUME)
game_music.play(loops=-1, fade_ms=1000)

alarm = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "alarm" / "loop_3.wav")
alarm.set_volume(0.3)

impact = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "impact" / "blast_1.wav")
impact.set_volume(0.5)

death_sound = pygame.mixer.Sound(
    settings.ASSETS_PATH / "sounds" / "impact" / "loose_1.wav"
)
death_sound.set_volume(0.2)

# Spieler initialisieren
player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))

# Zeitpunkt merken, an dem das Spiel gestartet ist
game_start_time = pygame.time.get_ticks()

# Asteroid Hilfsvariablen
last_asteroid_spawn = 0
asteroid_cooldown = 0# in ms

# API-Client vorbereiten und Spieler anlegen
api_client = ApiClient(settings.API_BASE_URL)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")

try:
    player_id = api_client.create_player(device_id, player_name)
except httpx.HTTPError:
    print("Konnte keine Verbindung zur API aufbauen. Der Score wird nicht gespeichert.")
    player_id = None

# Game Loop
running = True
while running:
    # 1. Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_music.set_volume(GAME_MUSIC_VOLUME * 0.2)
            pause_started = pygame.time.get_ticks()
            if not menu.pause_screen(background=display_surface.copy()):
                running = False
            game_music.set_volume(GAME_MUSIC_VOLUME)
            game_start_time += pygame.time.get_ticks() - pause_started
            clock.tick()  # Pause nicht in die nächste Delta Time einrechnen

    # 2. Zeichenfläche zurücksetzen
    display_surface.blit(background)

    # 3. Spiellogik aktualisieren
    time_lived = (pygame.time.get_ticks() - game_start_time) / 1000

    # Kollision: Projektile <-> Asteroiden
    projectile_asteroid_collisions = pygame.sprite.groupcollide(
        projectiles, asteroids, True, True
    )
    for destroyed_asteroids in projectile_asteroid_collisions.values():
        player.asteroids_destroyed += len(destroyed_asteroids)
        impact.play()

    # Kollision: Spieler <-> Asteroiden
    if pygame.sprite.spritecollide(player, asteroids, dokill=True):
        player.lives -= 1
        impact.play()
        if player.lives == 0:
            alarm.stop()
            game_music.stop()
            death_sound.play()

            if player_id is not None:
                try:
                    api_client.submit_score(
                        player_id, player.asteroids_destroyed, time_lived
                    )
                except httpx.HTTPError:
                    print("Score konnte nicht gesendet werden.")

            if menu.death_screen(
                player.asteroids_destroyed,
                time_lived,
                background=display_surface.copy(),
            ):
                # Neue Runde: Spielfeld leeren und Spielzustand zurücksetzen
                asteroids.empty()
                projectiles.empty()
                player = Player(
                    (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2)
                )
                game_start_time = pygame.time.get_ticks()
                last_asteroid_spawn = 0
                game_music.play(loops=-1, fade_ms=1000)
                clock.tick()  # Death-Screen nicht in die nächste Delta Time einrechnen
            else:
                running = False
            continue
        elif player.lives == 1:
            alarm.play()

    projectiles.update(delta_time)
    asteroids.update(delta_time)
    player.update(delta_time)

    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_spawn >= asteroid_cooldown:
        Asteroid()
        last_asteroid_spawn = current_time

    # 4. Objekte auf der Zeichenfläche zeichnen (Rendering)
    projectiles.draw(display_surface)
    asteroids.draw(display_surface)
    display_surface.blit(player.image, player.rect)
    draw_hud(player.lives, player.asteroids_destroyed, time_lived)

    # 5. Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # 6. Framerate limitieren und Delta Time berechnen
    delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden

# Anwendung sauber beenden
pygame.quit()
