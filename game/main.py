import settings
import pygame
import space_game_entities
from space_game_entities import Player

pygame.mixer.init()
space_game_entities.configure(settings.ASSETS_PATH)

pygame.init()
display_surface = pygame.display.set_mode(
    (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
)
pygame.display.set_caption("Space Shooter Game")
clock = pygame.time.Clock()
delta_time = 0
player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))
# Projektil definieren
projectile = pygame.Surface((10, 40))
projectile.fill("#4deeea")
projectile_rects = []
last_shot = pygame.time.get_ticks()  # in ms
running = True
while running:
    # 1. Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Zeichenfläche zurücksetzen
    display_surface.fill("#121212")

    # 3. Spiellogik aktualisieren
    player.updaite(delta_time)
    # Projektile bewegen
    for projectile_rect in projectile_rects:
        projectile_rect.y -= 800 * delta_time
    # Projektile außerhalb des Bildschirms entfernen
    projectile_rects = [rect for rect in projectile_rects if rect.bottom > 0]

    # 4. Objekte auf der Zeichenfläche zeichnen (Rendering)
    for projectile_rect in projectile_rects:
        display_surface.blit(projectile, projectile_rect)
        display_surface.blit(player.image, player.rect)

    # 5. Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # 6. Framerate limitieren und Delta Time berechnen
    delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden
pygame.quit()
