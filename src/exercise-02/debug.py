import pygame


pygame.init()
font = pygame.font.Font(size=40)


def debug(text: str, x: int = 10, y: int = 10):
    display_surface = pygame.display.get_surface()

    debug_surface = font.render(text, antialias=True, color="black")
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    display_surface.blit(debug_surface, debug_rect)
