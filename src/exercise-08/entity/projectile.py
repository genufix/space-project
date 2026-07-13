import pygame
import settings

projectiles = pygame.sprite.Group()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, spawn_position, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(
            settings.ASSETS_PATH / "images" / "projectile" / "red" / "laser_6.png"
        )
        self.rect = self.image.get_frect(midbottom=spawn_position)

        self.add(projectiles)

    def update(self, delta_time):
        self.rect.y -= 800 * delta_time

        # Projektil außerhalb des Bildschirms entfernen
        if self.rect.bottom < 0:
            self.kill()
