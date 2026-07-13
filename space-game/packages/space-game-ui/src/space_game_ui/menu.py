import math

import pygame

from space_game_ui.config import get_assets_path

BACKGROUND = "#121212"
ACCENT = "#4deeea"


class Menu:
    """Fertige Start-, Pause- und Death-Screen-Overlays für space-game.

    Jede *_screen()-Methode blockiert mit einer eigenen kleinen Event-Loop,
    bis der Spieler eine Entscheidung getroffen hat, und kann danach direkt
    in main.py weiterverwendet werden.
    """

    MAX_NAME_LENGTH = 16
    PANEL_SIZE = (640, 360)
    PANEL_RADIUS = 18

    def __init__(self, display_surface: pygame.Surface):
        self.display_surface = display_surface
        self.clock = pygame.time.Clock()
        font_path = get_assets_path() / "fonts" / "PressStart2P-Regular.ttf"
        self.title_font = pygame.font.Font(font_path, 36)
        self.font = pygame.font.Font(font_path, 20)
        self.small_font = pygame.font.Font(font_path, 14)

        if pygame.mixer.get_init() is None:
            raise RuntimeError(
                "pygame.mixer ist noch nicht initialisiert. Rufe pygame.mixer.init() auf, "
                "bevor du Menu(display_surface) erzeugst."
            )
        self.menu_music = pygame.mixer.Sound(
            get_assets_path() / "music" / "menu" / "space_cadet.ogg"
        )
        self.menu_music.set_volume(0.2)
        self.confirm_sound = pygame.mixer.Sound(
            get_assets_path() / "sounds" / "ui" / "confirmation_1.wav"
        )
        self.confirm_sound.set_volume(0.1)

    def start_screen(
        self, title: str = "SPACE SHOOTER", background: pygame.Surface | None = None
    ) -> str | None:
        """Zeigt den Startbildschirm mit Namenseingabe.

        Gibt den eingegebenen Namen zurück, oder None, falls das Fenster geschlossen wurde.
        """
        player_name = ""
        music_channel = self.menu_music.play(loops=-1, fade_ms=500)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._stop_music(music_channel)
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name.strip():
                        self.confirm_sound.play()
                        self._stop_music(music_channel)
                        return player_name.strip()
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    elif (
                        event.unicode.isprintable()
                        and len(player_name) < self.MAX_NAME_LENGTH
                    ):
                        player_name += event.unicode

            self._draw_overlay(background)
            self._draw_center_text(title, self.title_font, -120, color=ACCENT)
            self._draw_divider(-80)
            self._draw_center_text("Dein Name:", self.small_font, -40)
            self._draw_center_text(player_name or "_", self.font, 0)
            self._draw_center_text("ENTER zum Starten", self.small_font, 80, pulse=True)

            pygame.display.flip()
            self.clock.tick(60)

    def pause_screen(self, background: pygame.Surface | None = None) -> bool:
        """Zeigt den Pause-Bildschirm.

        Gibt True zurück, wenn weitergespielt werden soll, sonst False.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.confirm_sound.play()
                        return True
                    if event.key == pygame.K_q:
                        self.confirm_sound.play()
                        return False

            self._draw_overlay(background)
            self._draw_center_text("PAUSE", self.title_font, -40, color=ACCENT)
            self._draw_divider(0)
            self._draw_center_text(
                "ESC = Weiter    Q = Beenden", self.small_font, 40, pulse=True
            )

            pygame.display.flip()
            self.clock.tick(60)

    def death_screen(
        self,
        asteroids_destroyed: int,
        time_lived: float,
        background: pygame.Surface | None = None,
    ) -> bool:
        """Zeigt den Death-Screen inklusive Score.

        Gibt True zurück, wenn ein neues Spiel gestartet werden soll, sonst False.
        """
        music_channel = self.menu_music.play(loops=-1, fade_ms=500)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._stop_music(music_channel)
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.confirm_sound.play()
                        self._stop_music(music_channel)
                        return True
                    if event.key == pygame.K_ESCAPE:
                        self.confirm_sound.play()
                        self._stop_music(music_channel)
                        return False

            self._draw_overlay(background)
            self._draw_center_text("GAME OVER", self.title_font, -100, color=ACCENT)
            self._draw_divider(-60)
            self._draw_center_text(
                f"Asteroiden zerstört: {asteroids_destroyed}", self.font, -20
            )
            # Kein führendes "Ü": Großbuchstaben-Umlaute wirken in diesem Pixel-Font wie Kleinbuchstaben.
            self._draw_center_text(f"Zeit: {time_lived:.1f} Sekunden", self.font, 20)
            self._draw_center_text(
                "ENTER = Neustart    ESC = Beenden", self.small_font, 90, pulse=True
            )

            pygame.display.flip()
            self.clock.tick(60)

    @staticmethod
    def _stop_music(channel: pygame.mixer.Channel | None) -> None:
        # Sound.play() kann None liefern, wenn gerade kein Mixer-Kanal frei ist.
        if channel is not None:
            channel.stop()

    def _draw_overlay(self, background: pygame.Surface | None = None) -> None:
        if background is not None:
            self.display_surface.blit(background, (0, 0))
        else:
            self.display_surface.fill(BACKGROUND)

        dim = pygame.Surface(self.display_surface.get_size(), pygame.SRCALPHA)
        dim.fill((0, 0, 0, 160))
        self.display_surface.blit(dim, (0, 0))

        panel_rect = pygame.Rect((0, 0), self.PANEL_SIZE)
        panel_rect.center = self.display_surface.get_rect().center

        self._draw_glow(panel_rect)

        # Halbtransparentes Panel mit abgerundeten Ecken - das abgedunkelte Spiel
        # bleibt dahinter leicht sichtbar, statt von einem schwarzen Block verdeckt zu werden.
        panel = pygame.Surface(panel_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(
            panel, (8, 14, 18, 215), panel.get_rect(), border_radius=self.PANEL_RADIUS
        )
        accent = pygame.Color(ACCENT)
        pygame.draw.rect(
            panel,
            (accent.r, accent.g, accent.b, 160),
            panel.get_rect(),
            width=2,
            border_radius=self.PANEL_RADIUS,
        )
        self.display_surface.blit(panel, panel_rect)

    def _draw_glow(self, panel_rect: pygame.Rect, margin: int = 48) -> None:
        # Weicher Schein: ein kleines, hartes Rechteck wird per smoothscale() hochskaliert -
        # die Interpolation verwischt die Kanten zu einem sanften Verlauf (billiger Blur).
        accent = pygame.Color(ACCENT)
        scale = 24
        glow_size = (panel_rect.width + margin * 2, panel_rect.height + margin * 2)

        small = pygame.Surface(
            (glow_size[0] // scale, glow_size[1] // scale), pygame.SRCALPHA
        )
        inner = small.get_rect().inflate(
            -2 * (margin // scale) - 2, -2 * (margin // scale) - 2
        )
        pygame.draw.rect(
            small, (accent.r, accent.g, accent.b, 110), inner, border_radius=2
        )

        glow = pygame.transform.smoothscale(small, glow_size)

        # Panel-Fläche wieder ausstanzen, damit der Schein nur außen um den Rahmen liegt
        # und nicht durch das halbtransparente Panel hindurchleuchtet.
        panel_area = pygame.Rect((0, 0), panel_rect.size)
        panel_area.center = glow.get_rect().center
        pygame.draw.rect(
            glow, (0, 0, 0, 0), panel_area, border_radius=self.PANEL_RADIUS
        )

        self.display_surface.blit(glow, glow.get_rect(center=panel_rect.center))

    def _draw_divider(self, y_offset: int, width_ratio: float = 0.6) -> None:
        panel_rect = pygame.Rect((0, 0), self.PANEL_SIZE)
        panel_rect.center = self.display_surface.get_rect().center

        line_width = panel_rect.width * width_ratio
        center_x = self.display_surface.get_width() / 2
        y = self.display_surface.get_height() / 2 + y_offset

        pygame.draw.line(
            self.display_surface,
            ACCENT,
            (center_x - line_width / 2, y),
            (center_x + line_width / 2, y),
            2,
        )

    def _draw_center_text(
        self,
        text: str,
        font: pygame.font.Font,
        y_offset: int,
        color: str = "white",
        pulse: bool = False,
    ) -> None:
        surface = font.render(text, True, color)
        if pulse:
            surface.set_alpha(155 + int(100 * math.sin(pygame.time.get_ticks() / 300)))

        center = (
            self.display_surface.get_width() / 2,
            self.display_surface.get_height() / 2 + y_offset,
        )
        self.display_surface.blit(surface, surface.get_rect(center=center))
