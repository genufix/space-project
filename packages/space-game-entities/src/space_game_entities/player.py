import pygame

from enum import Enum
from space_game_entities.config import get_assets_path
from space_game_entities.projectile import Projectile

THRUST = 900
THRUST_FRAME_DURATION = 90  # ms pro Flammen-Frame (fire01 -> fire02 -> fire03, geloopt)


class ShipType(Enum):
    CLASSIC = "classic"
    FIGHTER = "fighter"
    STEALTH = "stealth"


class ShipColor(Enum):
    BLUE = "blue"
    GREEN = "green"
    ORANGE = "orange"
    RED = "red"


class Player(pygame.sprite.Sprite):
    """Steuerbares Spielerschiff (WASD bewegt, SPACE schießt mit `cooldown` ms Pause).

    Startet mit 4 Leben (`self.lives`) - bei 3/2/1 wird automatisch eine passende
    Schadensanzeige über dem Rumpf eingeblendet. Mit `physics_world` übernimmt pymunk
    die Bewegung inkl. Trägheit (Aufgabe 11).
    """

    def __init__(
        self,
        position: tuple[float, float],
        *groups,
        ship: ShipType = ShipType.CLASSIC,
        color: ShipColor = ShipColor.BLUE,
        speed: float = 450,
        cooldown: int = 500,
        physics_world=None,
    ):
        super().__init__(*groups)

        assets_path = get_assets_path()

        self.hull = pygame.image.load(
            assets_path / "images" / "ship" / ship.value / f"{color.value}.png"
        ).convert_alpha()
        self.damage_overlays = {
            3: pygame.image.load(
                assets_path
                / "images"
                / "ship"
                / ship.value
                / "overlay"
                / "damage_1.png"
            ).convert_alpha(),
            2: pygame.image.load(
                assets_path
                / "images"
                / "ship"
                / ship.value
                / "overlay"
                / "damage_2.png"
            ).convert_alpha(),
            1: pygame.image.load(
                assets_path
                / "images"
                / "ship"
                / ship.value
                / "overlay"
                / "damage_3.png"
            ).convert_alpha(),
        }

        self.thrust_frames = [
            pygame.image.load(
                assets_path / "images" / "ship" / "thrust" / f"fire0{i}.png"
            ).convert_alpha()
            for i in (1, 2, 3)
        ]
        thrust_height = max(frame.get_height() for frame in self.thrust_frames)

        # Kollisions-/Physik-Hitbox bleibt immer an der Rumpfgröße orientiert, auch wenn
        # self.image durch die Flamme darunter größer ist (blit() nutzt nur rect.topleft).
        self.rect = self.hull.get_frect(center=position)

        self.image = pygame.Surface(
            (self.hull.get_width(), self.hull.get_height() + thrust_height),
            pygame.SRCALPHA,
        )
        self.is_thrusting = False
        self.thrust_frame_index = 0
        self.thrust_animation_timer = 0

        self.speed = speed
        self.cooldown = cooldown
        self.direction = pygame.math.Vector2()
        self.last_shot = 0
        # 4 Leben, damit alle 3 Schadensanzeigen (damage_1/2/3) auch tatsächlich einen beschädigten
        # Zustand zeigen - bei vollen Leben (4) ist keine Schadensanzeige eingeblendet.
        self.lives = 4
        self.asteroids_destroyed = 0
        self._compose_image()

        self.projectile_sound = pygame.mixer.Sound(
            assets_path / "sounds" / "laser" / "bullet_2.wav"
        )
        self.projectile_sound.set_volume(0.2)

        self.physics_world = physics_world
        if physics_world is not None:
            self.physics_body = physics_world.add_circle(
                position=position, radius=self.rect.width / 2, velocity=(0, 0)
            )

    def update(self, delta_time: float):
        keys = pygame.key.get_pressed()

        self.direction.update(0, 0)
        if keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_s]:
            self.direction.y += 1
        if keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_d]:
            self.direction.x += 1

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        if self.physics_world is not None:
            self._update_physics_movement(delta_time)
        else:
            self.rect.center += self.direction * self.speed * delta_time
            self._wrap_screen()

        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot >= self.cooldown:
                Projectile(self.rect.midtop)
                self.projectile_sound.play()
                self.last_shot = current_time

        self._update_thrust_animation(delta_time)
        self._compose_image()

    def _wrap_screen(self):
        display_surface = pygame.display.get_surface()
        width, height = display_surface.get_size()

        wrapped = False
        if self.rect.left > width:
            self.rect.right = 0
            wrapped = True
        elif self.rect.right < 0:
            self.rect.left = width
            wrapped = True

        if self.rect.top > height:
            self.rect.bottom = 0
            wrapped = True
        elif self.rect.bottom < 0:
            self.rect.top = height
            wrapped = True

        if wrapped and self.physics_world is not None:
            self.physics_body.sync_from_rect(self.rect)

    def _update_physics_movement(self, delta_time):
        thrust = self.direction * THRUST * delta_time

        current_velocity = self.physics_body.velocity
        new_velocity = pygame.math.Vector2(current_velocity.x, current_velocity.y)
        new_velocity += thrust

        if new_velocity.length() > self.speed:
            new_velocity.scale_to_length(self.speed)

        self.physics_body.velocity = (new_velocity.x, new_velocity.y)
        self.physics_body.sync_rect(self.rect)
        self._wrap_screen()

    def _update_thrust_animation(self, delta_time):
        self.is_thrusting = self.direction.length_squared() > 0
        if not self.is_thrusting:
            self.thrust_animation_timer = 0
            self.thrust_frame_index = 0
            return

        self.thrust_animation_timer += delta_time * 1000
        if self.thrust_animation_timer >= THRUST_FRAME_DURATION:
            self.thrust_animation_timer = 0
            self.thrust_frame_index = (self.thrust_frame_index + 1) % len(
                self.thrust_frames
            )

    def _compose_image(self):
        self.image.fill((0, 0, 0, 0))
        self.image.blit(self.hull, (0, 0))

        damage_overlay = self.damage_overlays.get(self.lives)
        if damage_overlay is not None:
            self.image.blit(damage_overlay, (0, 0))

        if self.is_thrusting:
            flame = self.thrust_frames[self.thrust_frame_index]
            flame_rect = flame.get_rect(
                midtop=(self.hull.get_width() / 2, self.hull.get_height())
            )
            self.image.blit(flame, flame_rect)
