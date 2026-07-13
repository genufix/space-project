import pygame

from space_game_entities.config import get_assets_path

projectiles = pygame.sprite.Group()

SPEED = 800
UP = pygame.math.Vector2(0, -1)


class Projectile(pygame.sprite.Sprite):
    """Laser-Schuss. Fliegt standardmäßig gerade nach oben und entfernt sich selbst,
    sobald er den Bildschirm verlässt. Mit `direction` fliegt (und dreht) er sich in
    eine beliebige Richtung - so schießt z.B. der Enemy im Showcase nach unten."""

    def __init__(
        self,
        position: tuple[float, float],
        *groups,
        direction: pygame.math.Vector2 | tuple[float, float] | None = None,
        color: str = "blue",
        owner: pygame.sprite.Sprite | None = None,
    ):
        super().__init__(projectiles, *groups)

        # Wer geschossen hat (z.B. ein Enemy) - damit lässt sich verhindern, dass ein Schuss
        # sein eigenes Schiff trifft, bevor er sich vom Abschusspunkt wegbewegt hat.
        self.owner = owner

        base_image = pygame.image.load(
            get_assets_path() / "images" / "projectile" / color / "laser_7.png"
        ).convert_alpha()

        if direction is None:
            # Standardfall (Spieler-Schuss): unrotiert nach oben, wie bisher.
            self.direction = pygame.math.Vector2(UP)
            self.image = base_image
            self.rect = self.image.get_frect(midbottom=position)
        else:
            # Beliebige Richtung (z.B. Gegner, der auf den Spieler zielt) -
            # Bild wird passend zur Flugrichtung gedreht.
            self.direction = pygame.math.Vector2(direction)
            if self.direction.length_squared() > 0:
                self.direction = self.direction.normalize()
            angle = UP.angle_to(self.direction)
            self.image = pygame.transform.rotate(base_image, -angle)
            self.rect = self.image.get_frect(center=position)

    def update(self, delta_time: float):
        self.rect.center += self.direction * SPEED * delta_time

        display_surface = pygame.display.get_surface()
        width, height = display_surface.get_size()
        if (
            self.rect.bottom < 0
            or self.rect.top > height
            or self.rect.right < 0
            or self.rect.left > width
        ):
            self.kill()
