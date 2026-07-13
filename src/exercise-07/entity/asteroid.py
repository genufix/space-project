import pygame
import settings
from random import randint, uniform

asteroids = pygame.sprite.Group()


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # Zufällige Position
        x = randint(0, settings.WINDOW_WIDTH)
        y = randint(-300, -80)

        self.image = pygame.Surface((80, 80))
        self.rect = self.image.get_frect(center=(x, y))

        # Zufällige Geschwindigkeit
        self.velocity = randint(200, 400)

        # Zufällige Richtung
        self.direction = pygame.math.Vector2(uniform(-1, 1), 1)
        self.direction = self.direction.normalize()

        self.add(asteroids)

    def update(self, delta_time):
        self.rect.center += self.direction * self.velocity * delta_time

        # Asteroid außerhalb des Bildschirms entfernen
        if (
            self.rect.top > settings.WINDOW_HEIGHT
            or self.rect.right < 0
            or self.rect.left > settings.WINDOW_WIDTH
        ):
            self.kill()
