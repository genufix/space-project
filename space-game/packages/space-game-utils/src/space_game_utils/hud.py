import pygame

from space_game_utils.config import get_assets_path

MAX_LIVES = 4
MARGIN = 24
HEART_FULL = "#ff4d6d"
HEART_LOST = "#3a3a3a"

_font = None


def _get_font():
    global _font
    if _font is None:
        pygame.font.init()
        _font = pygame.font.Font(
            get_assets_path() / "fonts" / "PressStart2P-Regular.ttf", 20
        )
    return _font


def draw_hud(
    lives: int, asteroids_destroyed: int, time_lived: float, max_lives: int = MAX_LIVES
):
    """Zeichnet Leben (Herz-Slots), zerstörte Asteroiden und Zeit oben auf die Display Surface.

    Benötigt ein vorheriges space_game_utils.configure(settings.ASSETS_PATH) für den Font.
    `max_lives` muss zum Startwert von `player.lives` passen (Standard: 4).
    """
    display_surface = pygame.display.get_surface()

    _draw_lives(display_surface, lives, max_lives)
    _draw_stat(
        display_surface, f"ASTEROIDEN {asteroids_destroyed:03d}", anchor="midtop"
    )
    _draw_stat(display_surface, f"ZEIT {time_lived:06.1f}", anchor="topright")


def _draw_lives(display_surface: pygame.Surface, lives: int, max_lives: int):
    # Feste Anzahl Herz-Slots statt einer Zahl - kein Springen, egal wie viele Leben übrig sind.
    font = _get_font()
    hearts = "".join("♥ " for _ in range(max_lives))[:-1]
    heart_surface = font.render(hearts, antialias=True, color=HEART_LOST)
    heart_surface.blit(
        font.render(
            hearts[: lives * 2 - 1] if lives else "", antialias=True, color=HEART_FULL
        ),
        (0, 0),
    )
    display_surface.blit(
        heart_surface, heart_surface.get_rect(topleft=(MARGIN, MARGIN))
    )


def _draw_stat(display_surface: pygame.Surface, text: str, anchor: str):
    # Monospace-Font: jede Ziffer ist gleich breit, deshalb "springt" der Text beim Hochzählen nicht.
    font = _get_font()
    stat_surface = font.render(text, antialias=True, color="white")
    display_surface_size = display_surface.get_size()

    if anchor == "midtop":
        rect = stat_surface.get_rect(midtop=(display_surface_size[0] / 2, MARGIN))
    else:
        rect = stat_surface.get_rect(
            topright=(display_surface_size[0] - MARGIN, MARGIN)
        )

    display_surface.blit(stat_surface, rect)
