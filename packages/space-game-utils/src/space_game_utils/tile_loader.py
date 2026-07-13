import pygame
from os import PathLike
from pathlib import Path


def load_background(path: str | PathLike) -> pygame.Surface:
    # Display-Größe holen (z.B. 1280x720)
    display_surface = pygame.display.get_surface()

    # Fehler ausgeben, falls Funktion an falscher Position aufgerufen wird
    if display_surface is None:
        raise RuntimeError(
            "No display surface available. Call pygame.display.set_mode() before this function."
        )

    display_width, display_height = display_surface.get_size()

    # Pfad und Tile laden
    tile = pygame.image.load(Path(path)).convert()
    tile_width, tile_height = tile.get_size()

    # Berechnen, wie oft wir das Tile in x- und y-Richtung brauchen
    tiles_x = (display_width // tile_width) + 1
    tiles_y = (display_height // tile_height) + 1

    # Neue Surface erzeugen und kacheln
    background = pygame.Surface((display_width, display_height)).convert()

    for y in range(tiles_y):
        for x in range(tiles_x):
            background.blit(tile, (x * tile_width, y * tile_height))

    return background
