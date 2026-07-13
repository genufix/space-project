import pygame
from enum import Enum
from random import choice, randint, uniform

from space_game_entities.config import get_assets_path

asteroids = pygame.sprite.Group()


class AsteroidSize(Enum):
    BIG = "big"
    MEDIUM = "med"


VARIANTS = {
    AsteroidSize.MEDIUM: {
        "images": ("med_1.png", "med_2.png"),
        "speed_range": (220, 320),
    },
    AsteroidSize.BIG: {
        "images": ("big_1.png", "big_2.png", "big_3.png", "big_4.png"),
        "speed_range": (150, 250),
    },
}
# Trefferpunkte, bevor ein Asteroid zerstört wird (bei take_damage(), siehe unten).
HIT_POINTS = {
    AsteroidSize.BIG: 2,
    AsteroidSize.MEDIUM: 1,
}
# In welche Größe sich ein zerstörter Asteroid aufteilt (MEDIUM zerspringt nicht weiter).
SPLITS_INTO = {
    AsteroidSize.BIG: AsteroidSize.MEDIUM,
}
COLORS = ("grey", "brown")

# Wie stark sich die Geschwindigkeit beim Splitten (siehe take_damage()) reduziert, statt die
# volle (meist höhere) Geschwindigkeit der kleineren Variante zu übernehmen.
SPLIT_SPEED_FACTOR = 0.5
MIN_SPLIT_SPEED = 60


class Asteroid(pygame.sprite.Sprite):
    """Asteroid mit zufälliger Größe, Farbe, Bild-Variante, Richtung und Geschwindigkeit.

    Ohne Argumente (`Asteroid()`, siehe Aufgabe 6) spawnt er oberhalb des Bildschirms und
    fliegt nach unten. Alle Eigenschaften lassen sich per Keyword-Argument festlegen; mit
    `physics_world` übernimmt pymunk die Bewegung (Aufgabe 11).
    """

    def __init__(
        self,
        *groups,
        size: AsteroidSize | None = None,
        position: tuple[float, float] | None = None,
        color: str | None = None,
        direction: pygame.math.Vector2 | tuple[float, float] | None = None,
        speed: float | None = None,
        physics_world=None,
    ):
        super().__init__(asteroids, *groups)

        assets_path = get_assets_path()
        width = pygame.display.get_surface().get_width()

        self.size = size if size is not None else choice(list(AsteroidSize))
        self.color = color if color is not None else choice(COLORS)
        self.hit_points = HIT_POINTS[self.size]
        variant = VARIANTS[self.size]

        self.image = pygame.image.load(
            assets_path / "images" / "asteroid" / self.color / choice(variant["images"])
        ).convert_alpha()

        if position is None:
            # Kein Startpunkt übergeben -> klassischer Spawn von oben (siehe Aufgabe 6).
            position = (randint(0, width), randint(-300, -80))
        x, y = position
        self.rect = self.image.get_frect(center=(x, y))

        if direction is None:
            direction = pygame.math.Vector2(uniform(-1, 1), 1)
        self.direction = pygame.math.Vector2(direction).normalize()

        if speed is None:
            speed = randint(*variant["speed_range"])

        self.physics_world = physics_world
        self.physics_body = None
        if physics_world is not None:
            self.physics_body = physics_world.add_circle(
                position=(x, y),
                radius=self.rect.width / 2,
                velocity=(self.direction.x * speed, self.direction.y * speed),
            )
        else:
            self.velocity = speed

    def update(self, delta_time: float):
        display_surface = pygame.display.get_surface()
        width, height = display_surface.get_size()

        if self.physics_world is not None:
            self.physics_body.sync_rect(self.rect)
        else:
            self.rect.center += self.direction * self.velocity * delta_time

        # -400 lässt Platz für die Spawn-Zone oberhalb des Bildschirms (y bis -300, siehe oben) -
        # nur wer darüber hinaus nach oben entkommt (Split-Kinder, Physik), wird entfernt.
        if (
            self.rect.top > height
            or self.rect.right < 0
            or self.rect.left > width
            or self.rect.bottom < -400
        ):
            self.kill()

    def take_damage(self, amount=1):
        """Reduziert die Trefferpunkte um `amount`.

        Gibt True zurück, wenn der Asteroid dadurch zerstört wurde - bei BIG entstehen dabei
        automatisch zwei MEDIUM-Asteroiden an der aktuellen Position, MEDIUM verschwindet
        endgültig. Bestehende Aufgaben nutzen weiterhin direkt `.kill()` (z.B. über
        `groupcollide(..., dokill=True)`) und bleiben davon unberührt, da diese Methode nur
        aufgerufen wird, wenn sie explizit genutzt wird.
        """
        self.hit_points -= amount
        if self.hit_points > 0:
            return False

        next_size = SPLITS_INTO.get(self.size)
        if next_size is not None:
            if self.physics_world is not None:
                current_speed = pygame.math.Vector2(self.physics_body.velocity).length()
            else:
                current_speed = self.velocity
            child_speed = max(current_speed * SPLIT_SPEED_FACTOR, MIN_SPLIT_SPEED)

            for _ in range(2):
                child_direction = pygame.math.Vector2(1, 0).rotate(uniform(0, 360))
                Asteroid(
                    size=next_size,
                    position=self.rect.center,
                    color=self.color,
                    direction=child_direction,
                    speed=child_speed,
                    physics_world=self.physics_world,
                )

        self.kill()
        return True

    def kill(self):
        # physics_body auf None setzen, damit ein doppeltes kill() (z.B. im selben Frame von
        # zwei Kollisions-Checks mit dokill=True) den Body nicht zweimal entfernen will.
        if self.physics_body is not None:
            self.physics_world.remove(self.physics_body)
            self.physics_body = None
        super().kill()
