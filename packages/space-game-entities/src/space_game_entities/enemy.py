import pygame
from random import choice, randint, uniform

from space_game_entities.config import get_assets_path
from space_game_entities.projectile import Projectile

enemies = pygame.sprite.Group()
enemy_projectiles = pygame.sprite.Group()

VARIANTS = ("enemy_1.png", "enemy_2.png")

SPEED = 160
COOLDOWN = 1800  # ms zwischen zwei Schüssen - deutlich träger als der Spieler
HIT_POINTS = 3
AVOID_RADIUS = 140  # Abstand, ab dem Asteroiden aktiv ausgewichen wird
RETARGET_INTERVAL = 2500  # ms bis zu einer neuen Patrouillen-Höhe
PATROL_TOP, PATROL_BOTTOM = 80, 260  # Band nahe des oberen Bildschirmrands
DOWN = pygame.math.Vector2(0, 1)


class Enemy(pygame.sprite.Sprite):
    """Gegnerisches Schiff für den Showcase - patrouilliert oben, weicht Asteroiden aus und
    schießt ausschließlich nach unten (keine gedrehten Schüsse). Um den Spieler damit trotzdem
    treffen zu können, versucht es stattdessen, sich horizontal über dem Spieler zu positionieren.
    """

    def __init__(self, *groups):
        super().__init__(enemies, *groups)

        assets_path = get_assets_path()
        self.image = pygame.image.load(
            assets_path / "images" / "enemy" / choice(VARIANTS)
        ).convert_alpha()

        width = pygame.display.get_surface().get_width()
        x = randint(0, width)
        self.rect = self.image.get_frect(center=(x, -self.image.get_height()))

        self.hit_points = HIT_POINTS
        # Ab jetzt zählen, nicht ab pygame-Start - sonst fällt der erste Schuss sofort
        # (und unsichtbar von außerhalb des Bildschirms), wenn das Spiel schon länger läuft.
        self.last_shot = pygame.time.get_ticks()
        self.retarget_timer = 0
        self.patrol_y = uniform(PATROL_TOP, PATROL_BOTTOM)

        self.projectile_sound = pygame.mixer.Sound(
            assets_path / "sounds" / "laser" / "bullet_1.wav"
        )
        self.projectile_sound.set_volume(0.15)

    def update(self, delta_time, player, asteroids):
        self._update_movement(delta_time, player, asteroids)
        self._wrap_screen()
        self._update_shooting()

    def take_damage(self, amount=1):
        """Reduziert die Trefferpunkte. Gibt True zurück, wenn der Gegner dadurch zerstört wurde."""
        self.hit_points -= amount
        if self.hit_points > 0:
            return False

        self.kill()
        return True

    def _update_movement(self, delta_time, player, asteroids):
        self.retarget_timer += delta_time * 1000
        if self.retarget_timer >= RETARGET_INTERVAL:
            self.retarget_timer = 0
            self.patrol_y = uniform(PATROL_TOP, PATROL_BOTTOM)

        position = pygame.math.Vector2(self.rect.center)
        # Da nur noch senkrecht nach unten geschossen wird, muss sich der Gegner selbst über
        # dem Spieler positionieren, statt frei zu patrouillieren.
        target = pygame.math.Vector2(player.rect.centerx, self.patrol_y)
        seek = target - position
        if seek.length_squared() > 0:
            seek = seek.normalize()

        avoidance = pygame.math.Vector2()
        for asteroid in asteroids:
            offset = position - pygame.math.Vector2(asteroid.rect.center)
            distance = offset.length()
            if 0 < distance < AVOID_RADIUS:
                avoidance += (
                    offset.normalize() * (AVOID_RADIUS - distance) / AVOID_RADIUS
                )

        direction = seek + avoidance * 2
        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.rect.center += direction * SPEED * delta_time

    def _wrap_screen(self):
        width = pygame.display.get_surface().get_width()

        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0

    def _update_shooting(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot < COOLDOWN:
            return

        Projectile(
            self.rect.midbottom,
            enemy_projectiles,
            direction=DOWN,
            color="red",
            owner=self,
        )
        self.projectile_sound.play()
        self.last_shot = current_time
