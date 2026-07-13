import pygame

_font = None


def _get_font() -> pygame.font.Font:
    global _font
    if _font is None:
        pygame.font.init()
        _font = pygame.font.Font(size=40)
    return _font


def debug(text: str, x: int = 10, y: int = 10) -> None:
    """Zeichnet `text` zum schnellen Testen auf den Bildschirm (Standard: oben links)."""
    display_surface = pygame.display.get_surface()
    if display_surface is None:
        raise RuntimeError(
            "Es gibt noch keine Display Surface. Rufe zuerst pygame.display.set_mode(...) auf, "
            "bevor du debug() verwendest."
        )

    # Weißer Text auf dunklem Kasten - so bleibt er auf jedem Hintergrund lesbar.
    debug_surface = _get_font().render(
        text, antialias=True, color="white", bgcolor="black"
    )
    display_surface.blit(debug_surface, debug_surface.get_rect(topleft=(x, y)))
