import pygame

projectiles = pygame.sprite.Group()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, spawn_position, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface((10, 40))
        self.rect = self.image.get_frect(midbottom=spawn_position)

        self.add(projectiles)

    def update(self, delta_time):
        self.rect.y -= 800 * delta_time
