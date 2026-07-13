import settings
import pygame
import space_game_entities
import space_game_utils
from space_game_entities import Player, projectiles, Asteroid, asteroids
from space_game_utils import draw_hud

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

# Spieler initialisieren
player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))

# Zeitpunkt merken, an dem das Spiel gestartet ist
game_start_time = pygame.time.get_ticks()

# Asteroid Hilfsvariablen
last_asteroid_spawn = 0
asteroid_cooldown = 1000  # in ms

# Game Loop
running = True
while running:
    # 1. Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Zeichenfläche zurücksetzen
    display_surface.fill("#121212")

    # 3. Spiellogik aktualisieren
    time_lived = (pygame.time.get_ticks() - game_start_time) / 1000

    # Kollision: Projektile <-> Asteroiden
    projectile_asteroid_collisions = pygame.sprite.groupcollide(
        projectiles, asteroids, True, True
    )
    for destroyed_asteroids in projectile_asteroid_collisions.values():
        player.asteroids_destroyed += len(destroyed_asteroids)

    # Kollision: Spieler <-> Asteroiden
    if pygame.sprite.spritecollide(player, asteroids, dokill=True):
        player.lives -= 1
        if player.lives == 0:
            running = False

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
