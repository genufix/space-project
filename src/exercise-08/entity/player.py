import pygame
import settings
from entity.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(
            settings.ASSETS_PATH / "images" / "ship" / "classic" / "red.png"
        ).convert_alpha()
        self.rect = self.image.get_frect(center=position)

        self.last_shot = 0
        self.asteroids_destroyed = 0
        self.lives = 3

        self.direction = pygame.Vector2()
        self.velocity = 440

        self.projectile_sound = pygame.mixer.Sound(
            settings.ASSETS_PATH / "sounds" / "laser" / "bullet_2.wav"
        )
        self.projectile_sound.set_volume(0.2)

    def update(self, delta_time):
        # Liste aller Tasten (gedrückt / nicht gedrückt)
        keys = pygame.key.get_pressed()

        # Vektor auf (0, 0) setzen
        self.direction.update(0, 0)

        # Tasten-Abfrage, um Spieler zu bewegen)
        if keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_d]:
            self.direction.x += 1

        if self.direction.length() >= 1:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.velocity * delta_time

        # Tasten-Abfrage, um Projektil zu erstellen
        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()  # in ms

            if current_time - self.last_shot >= 500:
                Projectile(self.rect.midtop)
                self.projectile_sound.play()
                self.last_shot = current_time

        # Bildschirmbegrenzung
        if self.rect.left > settings.WINDOW_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = settings.WINDOW_WIDTH

        if self.rect.top > settings.WINDOW_HEIGHT:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = settings.WINDOW_HEIGHT
