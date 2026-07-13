# space-game-physics

Ein leichtgewichtiger Wrapper um [pymunk](http://www.pymunk.org/), damit im `space-game`-Praktikum echte  
Physik (z. B. elastische Kollisionen zwischen Asteroiden) genutzt werden kann, ohne die rohe pymunk-API lernen zu müssen.

Wird in [Aufgabe 11](../../exercises/exercise-11/README.md) fertig in `game/main.py` eingebunden.

```python
from space_game_physics import PhysicsWorld

world = PhysicsWorld()

asteroid_body = world.add_circle(position=(x, y), radius=40, velocity=(50, 100))

# in der Game Loop:
world.step(delta_time)
asteroid_body.sync_rect(asteroid.rect)
```
