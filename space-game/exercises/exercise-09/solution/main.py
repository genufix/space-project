import httpx
import pygame
import settings
import space_game_entities
import space_game_utils
from space_game_entities import Player, projectiles, Asteroid, asteroids
from space_game_utils import load_background, get_device_id, ApiClient, draw_hud

# Grundlegendes Setup
pygame.init()

# Mixer initialisieren (Player lädt bereits jetzt einen Schuss-Sound)
pygame.mixer.init()

# space-game-entities und space-game-utils mitteilen, wo die Assets liegen
space_game_entities.configure(settings.ASSETS_PATH)
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

# Hintergrund laden
background = load_background(
    settings.ASSETS_PATH / "images" / "background" / "starfield" / "tile_1.png"
)

# Sounds laden
game_music = pygame.mixer.Sound(
    settings.ASSETS_PATH / "music" / "synthwave" / "loop_7.mp3"
)
game_music.set_volume(0.5)
game_music.play(loops=-1, fade_ms=1000)

alarm = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "alarm" / "loop_3.wav")
alarm.set_volume(0.3)

impact = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "impact" / "blast_1.wav")
impact.set_volume(0.5)

# Spieler initialisieren
player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))

# Zeitpunkt merken, an dem das Spiel gestartet ist
game_start_time = pygame.time.get_ticks()

# Asteroid Hilfsvariablen
last_asteroid_spawn = 0
asteroid_cooldown = 1000  # in ms

# API-Client vorbereiten und Spieler anlegen
api_client = ApiClient(settings.API_BASE_URL)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")
player_name = input("Wie lautet dein Name? ")

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
            running = False

            if player_id is not None:
                try:
                    api_client.submit_score(
                        player_id, player.asteroids_destroyed, time_lived
                    )
                except httpx.HTTPError:
                    print("Score konnte nicht gesendet werden.")
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
