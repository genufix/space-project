import httpx
import pygame
import settings
import space_game_entities
import space_game_ui
import space_game_utils
from space_game_entities import (
    Player,
    projectiles,
    Asteroid,
    asteroids,
    Enemy,
    enemies,
    enemy_projectiles,
    Explosion,
    explosions,
    HitExplosion,
    hit_explosions,
)
from space_game_physics import PhysicsWorld
from space_game_utils import load_background, get_device_id, ApiClient, draw_hud
from space_game_ui import Menu

# Grundlegendes Setup
pygame.init()

# Mixer initialisieren (Menu spielt bereits eigene Sounds, Player/Enemy einen Schuss-Sound)
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

# Physik-Welten erzeugen
asteroid_world = PhysicsWorld()
player_world = PhysicsWorld(damping=0.15)

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

# Kleiner Treffer-Sound: derselbe Einschlag wie bei Zerstörungen, aber als eigenes,
# leiseres Sound-Objekt, damit einfache Treffer die "echten" Explosionen nicht übertönen
hit_sound = pygame.mixer.Sound(
    settings.ASSETS_PATH / "sounds" / "impact" / "blast_1.wav"
)
hit_sound.set_volume(0.25)

death_sound = pygame.mixer.Sound(
    settings.ASSETS_PATH / "sounds" / "impact" / "loose_1.wav"
)
death_sound.set_volume(0.2)

# Spieler initialisieren
player = Player(
    (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2),
    physics_world=player_world,
)

# Zeitpunkt merken, an dem das Spiel gestartet ist
game_start_time = pygame.time.get_ticks()

# Asteroid Hilfsvariablen
last_asteroid_spawn = 0
asteroid_cooldown = 1000  # in ms

# Enemy Hilfsvariablen
# Ab dem echten Spielstart zählen (nicht ab Programmstart) - sonst taucht der erste
# Gegner sofort auf, wenn man lange im Startmenü saß
last_enemy_spawn = pygame.time.get_ticks()
enemy_cooldown = 9000  # in ms - Gegner sollen selten auftauchen
MAX_ENEMIES = 2  # nie mehr als zwei gleichzeitig auf dem Bildschirm

# API-Client vorbereiten und Spieler anlegen
api_client = ApiClient(settings.API_BASE_URL)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")

try:
    player_id = api_client.create_player(device_id, player_name)
except httpx.HTTPError:
    print("Konnte keine Verbindung zur API aufbauen. Der Score wird nicht gespeichert.")
    player_id = None


def play_player_death_explosion(time_lived):
    """Zeigt die große Explosion an der Stelle, an der der Spieler gestorben ist, bevor der
    Death-Screen erscheint - das Schiff selbst wird dafür nicht mehr gezeichnet.
    """
    Explosion(player.rect.center)
    clock.tick()  # Zeit seit dem letzten Tick verwerfen, bevor wir eigene Frames messen

    while explosions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                explosions.empty()
                return

        display_surface.blit(background)
        asteroids.draw(display_surface)
        enemies.draw(display_surface)
        projectiles.draw(display_surface)
        explosions.draw(display_surface)
        draw_hud(player.lives, player.asteroids_destroyed, time_lived)
        pygame.display.flip()

        frame_time = clock.tick(settings.FRAMERATE) / 1000
        explosions.update(frame_time)


def handle_player_hit(time_lived):
    """Ein Leben abziehen und - falls das letzte war - den Death-Screen zeigen.

    Auf dem Death-Screen startet ENTER eine neue Runde, ESC beendet das Spiel.
    Gibt True zurück, wenn die Game Loop danach per `continue` neu starten soll.
    """
    global running, player, game_start_time, last_asteroid_spawn, last_enemy_spawn

    player.lives -= 1
    impact.play()

    if player.lives == 0:
        alarm.stop()
        game_music.stop()
        death_sound.play()
        play_player_death_explosion(time_lived)

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
            for asteroid in asteroids.sprites():
                asteroid.kill()  # räumt auch den Physik-Body aus der Welt
            projectiles.empty()
            enemy_projectiles.empty()
            enemies.empty()
            hit_explosions.empty()
            player_world.remove(player.physics_body)
            player = Player(
                (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2),
                physics_world=player_world,
            )
            game_start_time = pygame.time.get_ticks()
            last_asteroid_spawn = 0
            last_enemy_spawn = pygame.time.get_ticks()
            game_music.play(loops=-1, fade_ms=1000)
            clock.tick()  # Death-Screen nicht in die nächste Delta Time einrechnen
        else:
            running = False
        return True

    if player.lives == 1:
        alarm.play()

    return False


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

    # Physik-Simulationen einen Schritt weiter berechnen
    asteroid_world.step(delta_time)
    player_world.step(delta_time)

    # Kollision: Projektile <-> Asteroiden (kleiner Treffer-Effekt bei jedem Treffer,
    # große Explosion nur, wenn der Asteroid dabei tatsächlich zerstört wird)
    asteroid_hits = pygame.sprite.groupcollide(projectiles, asteroids, True, False)
    for projectile, hit_asteroids in asteroid_hits.items():
        for asteroid in hit_asteroids:
            HitExplosion(projectile.rect.center)
            hit_sound.play()
            if asteroid.take_damage():
                Explosion(asteroid.rect.center)
                # Nur Spieler-Schüsse zählen für den Score (Enemy-Schüsse haben einen owner)
                if projectile.owner is None:
                    player.asteroids_destroyed += 1
                impact.play()

    # Kollision: Projektile <-> Gegner (ohne Auto-Kill, damit ein Schuss sein eigenes
    # Schiff nicht direkt beim Abschuss "trifft", solange er noch darüber liegt)
    potential_enemy_hits = pygame.sprite.groupcollide(
        projectiles, enemies, False, False
    )
    for projectile, hit_enemies in potential_enemy_hits.items():
        real_hits = [enemy for enemy in hit_enemies if enemy is not projectile.owner]
        if not real_hits:
            continue

        projectile.kill()
        HitExplosion(projectile.rect.center)
        hit_sound.play()
        for enemy in real_hits:
            if enemy.take_damage():
                Explosion(enemy.rect.center)
                impact.play()

    # Kollision: Spieler <-> Asteroiden
    if pygame.sprite.spritecollide(player, asteroids, dokill=True):
        if handle_player_hit(time_lived):
            continue

    # Kollision: Spieler <-> Gegner-Projektile
    if pygame.sprite.spritecollide(player, enemy_projectiles, dokill=True):
        if handle_player_hit(time_lived):
            continue

    # Kollision: Spieler <-> Gegner (Rammen) - der gerammte Gegner explodiert dabei sichtbar
    rammed_enemies = pygame.sprite.spritecollide(player, enemies, dokill=True)
    if rammed_enemies:
        for enemy in rammed_enemies:
            Explosion(enemy.rect.center)
            impact.play()
        if handle_player_hit(time_lived):
            continue

    projectiles.update(delta_time)  # bewegt auch die Gegner-Projektile mit
    asteroids.update(delta_time)
    enemies.update(delta_time, player, asteroids)
    explosions.update(delta_time)
    hit_explosions.update(delta_time)
    player.update(delta_time)

    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_spawn >= asteroid_cooldown:
        Asteroid(physics_world=asteroid_world)
        last_asteroid_spawn = current_time

    if len(enemies) < MAX_ENEMIES and current_time - last_enemy_spawn >= enemy_cooldown:
        Enemy()
        last_enemy_spawn = current_time

    # 4. Objekte auf der Zeichenfläche zeichnen (Rendering)
    asteroids.draw(display_surface)
    enemies.draw(display_surface)
    projectiles.draw(display_surface)
    explosions.draw(display_surface)
    hit_explosions.draw(display_surface)
    display_surface.blit(player.image, player.rect)
    draw_hud(player.lives, player.asteroids_destroyed, time_lived)

    # 5. Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # 6. Framerate limitieren und Delta Time berechnen
    delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden

# Anwendung sauber beenden
pygame.quit()
