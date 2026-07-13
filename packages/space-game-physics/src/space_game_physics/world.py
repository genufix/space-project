import pymunk


class PhysicsBody:
    """Kapselt einen pymunk-Body samt Shape und synct ihn mit einem pygame-Rect."""

    def __init__(self, body: pymunk.Body, shape: pymunk.Shape):
        self.body = body
        self.shape = shape

    @property
    def position(self) -> pymunk.Vec2d:
        return self.body.position

    @property
    def velocity(self) -> pymunk.Vec2d:
        return self.body.velocity

    @velocity.setter
    def velocity(self, value: tuple[float, float]) -> None:
        self.body.velocity = value

    def sync_rect(self, rect) -> None:
        """Setzt das Center eines pygame-Rects auf die aktuelle Physik-Position."""
        rect.center = (self.body.position.x, self.body.position.y)

    def sync_from_rect(self, rect) -> None:
        """Übernimmt das Center eines pygame-Rects als neue Physik-Position.

        Nötig, wenn die Position direkt am Rect verändert wurde (z. B. Screen-Wrap),
        damit die Physik-Simulation nicht die alte Position weiterverwendet.
        """
        self.body.position = rect.center


class PhysicsWorld:
    """Vereinfachter Zugriff auf eine pymunk.Space für space-game.

    Übernimmt das Erzeugen von Bodies/Shapes und das Stepping der Simulation,
    damit die rohe pymunk-API nicht selbst gelernt werden muss.
    """

    def __init__(self, gravity: tuple[float, float] = (0, 0), damping: float = 1.0):
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.space.damping = damping

    def step(self, delta_time: float) -> None:
        self.space.step(delta_time)

    def add_circle(
        self,
        position: tuple[float, float],
        radius: float,
        velocity: tuple[float, float] = (0, 0),
        mass: float = 1,
        elasticity: float = 0.9,
        friction: float = 0.0,
    ) -> PhysicsBody:
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment)
        body.position = position
        body.velocity = velocity

        shape = pymunk.Circle(body, radius)
        shape.elasticity = elasticity
        shape.friction = friction

        self.space.add(body, shape)
        return PhysicsBody(body, shape)

    def remove(self, physics_body: PhysicsBody) -> None:
        self.space.remove(physics_body.body, physics_body.shape)
