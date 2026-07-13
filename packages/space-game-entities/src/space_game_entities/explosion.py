import pygame

from space_game_entities.config import get_assets_path

explosions = pygame.sprite.Group()
hit_explosions = pygame.sprite.Group()

FRAME_SIZE = 48

_frame_cache = {}


def _load_frames(path_parts, scale):
    cache_key = (path_parts, scale)
    if cache_key not in _frame_cache:
        sheet = pygame.image.load(
            get_assets_path().joinpath(*path_parts)
        ).convert_alpha()
        frame_count = sheet.get_width() // FRAME_SIZE
        frames = []
        for i in range(frame_count):
            frame = sheet.subsurface((i * FRAME_SIZE, 0, FRAME_SIZE, FRAME_SIZE))
            frames.append(
                pygame.transform.scale_by(frame, scale) if scale != 1 else frame.copy()
            )
        _frame_cache[cache_key] = frames
    return _frame_cache[cache_key]


class _SpriteSheetAnimation(pygame.sprite.Sprite):
    """Spielt einmalig ein Sprite-Sheet an einer Position ab und entfernt sich danach selbst."""

    path_parts = ()
    default_group = None
    frame_duration = 40  # ms pro Frame
    scale = 1

    def __init__(self, position, *groups):
        super().__init__(self.default_group, *groups)

        self.frames = _load_frames(self.path_parts, self.scale)
        self.frame_index = 0
        self.animation_timer = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=position)

    def update(self, delta_time):
        self.animation_timer += delta_time * 1000
        if self.animation_timer < self.frame_duration:
            return

        self.animation_timer = 0
        self.frame_index += 1

        if self.frame_index >= len(self.frames):
            self.kill()
            return

        center = self.rect.center
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=center)


class Explosion(_SpriteSheetAnimation):
    """Größere Explosion (8 Frames) - gedacht für den tatsächlichen Tod eines Objekts (Asteroid,
    Enemy oder Player), nicht für jeden einzelnen Treffer.
    """

    path_parts = ("images", "asteroid", "explosion.png")
    default_group = explosions
    scale = 2
    frame_duration = 70


class HitExplosion(_SpriteSheetAnimation):
    """Kleiner Treffer-Effekt (7 Frames) - gedacht für jeden Projektil-Treffer, unabhängig davon,
    ob das getroffene Objekt dabei zerstört wird.
    """

    path_parts = ("images", "projectile", "hit_explosion.png")
    default_group = hit_explosions
    scale = 2
    frame_duration = 55
