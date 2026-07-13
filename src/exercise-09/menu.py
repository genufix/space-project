import pygame
import sys
from components.button import Button
from components.text_input import TextBlock

class MainMenu:

    def __init__(self, game_loop, display_surface):
        """Wir uebergeben hier das Fenster, sowie die Funktionen,
        welche im Menue abgerufen werden"""
        self.display_surface = display_surface
        self.game_loop = game_loop

        """Hier laden wir das Hintergrundbild fuer das Hauptmenue ins Programm"""
        self.bg = pygame.image.load("src/assets/blue_stars.png")

    def get_font(self, size):
        """Mit dieser Funktionen bekommen wir den gewuenschten TextFont"""
        return pygame.font.Font("src/assets/font.otf", size)

    def main_menu(self):
        """Erst Muessen wir die Groesse vom Bild an die Fenstergroesse anpassen
           Hierzu koennen wir erfragen wie gross das Fenster in x- und y- Richtunge ist"""

        x, y = self.display_surface.get_width(), self.display_surface.get_height()

        b_x = x / 2

        USER_NAME = TextBlock(pygame.image.load("src/assets/hover_rectangle.png"), (b_x, 400), self.get_font(75), "#d7fcd4", "violet")

        """Dann passen wir das Bild an diese Groesse an"""
        hintergrund = pygame.transform.scale(self.bg, (x,y))

        """Die Mausposition auf dem Bildschirm wird abgefragt, um zu
        erfahren, ob wir auf einem Button sind"""

        """Wir brauchen die x und y Position reletativ zur Groesse vom Fenster
           um die Buttons und Ueberschrift Mittig zu platzieren"""

        MENU_TEXT = self.get_font(100).render("Hauptmenue", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(b_x, 100))

        PLAY_BUTTON = Button(
            image=pygame.image.load("src/assets/hover_rectangle.png"),
            pos=(b_x, 250),
            text_input="Spielen",
            font=self.get_font(75),
            base_color="#d7fcd4",
            hovering_color="Violet",
        )

        while True:

            """Zum Schluss zeichnen wir das Hintergrundbild auf den Bildschirm"""
            self.display_surface.blit(hintergrund, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            self.display_surface.blit(MENU_TEXT, MENU_RECT)

            USER_NAME.update(self.display_surface)

            for button in [PLAY_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.display_surface)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                USER_NAME.handle_event(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.game_loop(USER_NAME.user_name)
                        USER_NAME.clear_name()
            pygame.display.flip()
