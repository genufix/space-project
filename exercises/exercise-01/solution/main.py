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

# Game Loop
running = True
while running:
    # 1. Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Zeichenfläche zurücksetzen
    display_surface.fill("white")

    # 3. TODO: Spiellogik aktualisieren

    # 4. TODO: Objekte auf der Zeichenfläche zeichnen (Rendering)

    # 5. Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # 6. Framerate limitieren
    clock.tick(FRAMERATE)

# Anwendung sauber beenden
pygame.quit()
