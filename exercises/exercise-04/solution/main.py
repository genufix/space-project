import pygame

# Grundlegendes Setup
pygame.init()

# Fenstergröße festlegen und Fenster erstellen
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Fenstertitel setzen
pygame.display.set_caption("Space Shooter")

# Framerate und Clock definieren
clock = pygame.time.Clock()
FRAMERATE = 60
delta_time = 0

# Quadrat definieren
square = pygame.Surface((200, 200))
square.fill("#7d37f0")
square_rect = square.get_frect()
square_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Projektil definieren
projectile = pygame.Surface((10, 40))
projectile.fill("#4deeea")
projectile_rects = []
last_shot = pygame.time.get_ticks()  # in ms

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
    keys = pygame.key.get_pressed()

    # Tasten-Abfrage, um Quadrat zu bewegen
    if keys[pygame.K_w]:
        square_rect.y -= 600 * delta_time
    if keys[pygame.K_s]:
        square_rect.y += 600 * delta_time
    if keys[pygame.K_a]:
        square_rect.x -= 600 * delta_time
    if keys[pygame.K_d]:
        square_rect.x += 600 * delta_time

    # Tasten-Abfrage, um Projektil zu erstellen
    if keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()  # in ms

        if current_time - last_shot >= 500:
            temp = projectile.get_frect(midbottom=(square_rect.midtop))
            projectile_rects.append(temp)
            last_shot = current_time

    # Projektile bewegen
    for projectile_rect in projectile_rects:
        projectile_rect.y -= 800 * delta_time

    # Projektile außerhalb des Bildschirms entfernen
    projectile_rects = [rect for rect in projectile_rects if rect.bottom > 0]

    # 4. Objekte auf der Zeichenfläche zeichnen (Rendering)
    for projectile_rect in projectile_rects:
        display_surface.blit(projectile, projectile_rect)

    display_surface.blit(square, square_rect)

    # 5. Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # 6. Framerate limitieren und Delta Time berechnen
    delta_time = clock.tick(FRAMERATE) / 1000  # ms -> Sekunden

# Anwendung sauber beenden
pygame.quit()
