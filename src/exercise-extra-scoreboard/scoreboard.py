import pygame
import imgkit
import io


class Scoreboard:
    def __init__(self, screen, url):
        """Das Fenster wird uebergeben"""
        self.display_surface = screen
        """Hier uebergeben wir die Web Addresse des Scoreboards,
          welche vom Webserver Team zur Verfuegung gestellt wird"""
        self.html_url = "https://python.org"
        self.bg = pygame.image.load("assets/blue_stars.png")

    def show_stats(self):
        """Erst Muessen wir die Groesse vom Bild an die Fenstergroesse anpassen
        Hierzu koennen wir erfragen wie gross das Fenster in x- und y- Richtunge ist"""
        x, y = self.display_surface.get_width(), self.display_surface.get_height()

        """Dann passen wir das Bild an diese Groesse an"""
        hintergrund = pygame.transform.scale(self.bg, (x, y))
        """Zum Schluss zeichnen wir das Hintergrundbild auf den Bildschirm"""
        self.display_surface.blit(hintergrund)

        """Die Website wird als Bild-Binary geladen"""
        image_data = imgkit.from_url(self.html_url, False, options={"format": "png"})
        print(type(image_data))

        """Die Datei muss noch umformatiert werden in ein lesbares Binary fuer pygame"""
        image_file = io.BytesIO(image_data)

        """Wir laden das Bild in pygame"""
        web_surface = pygame.image.load(image_file, "png")

        """Wir zentrieren das Bild in pygame"""
        web_surface_rect = web_surface.get_rect(
            center=(
                self.display_surface.get_width() // 2,
                self.display_surface.get_height() // 2,
            )
        )

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            self.display_surface.blit(web_surface, web_surface_rect)
            pygame.display.flip()
