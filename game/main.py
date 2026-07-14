import settings
import pygame
import space_game_entities
from space_game_entities import Player, projectiles, Asteroid, asteroids


# Grundlegendes Setup
pygame.init()

pygame.mixer.init()

space_game_entities.configure(settings.ASSETS_PATH)

display_surface = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
)
pygame.display.set_caption("Space Shooter")


clock = pygame.time.Clock()
delta_time = 0

player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))

last_asteroid_spawn = 0
asteroid_cooldown = 1000 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("#121212")
    projectiles.update(delta_time)
    player.update(delta_time)
    projectiles.draw(display_surface)
    asteroids.update(delta_time)
    asteroids.draw(display_surface)
    display_surface.blit(player.image, player.rect)

    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_spawn >= asteroid_cooldown:
      Asteroid()
      last_asteroid_spawn = current_time
    pygame.display.flip()

    
    delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden

pygame.quit()