# space-game-entities

Fertige `Player`-, `Projectile`- und `Asteroid`-Sprites für das `space-game`-Praktikum.

Dieses Package wird nicht selbst geschrieben, sondern ab [Aufgabe 5](../../exercises/exercise-05/README.md)
fertig in `game/main.py` eingebunden - inklusive zufälliger Asteroiden-Varianten (Größe & Farbe), einer
Schadensanzeige und einer Schubdüsen-Animation am Schiff, die beide automatisch mitlaufen (`Player` zeigt
`fire01.png` -> `fire02.png` -> `fire03.png` geloopt am Heck, sobald sich der Spieler bewegt - ohne dass sich
dafür etwas an der Kollisions-Hitbox ändert).

```python
import settings
import space_game_entities
from space_game_entities import (
    Player, ShipType, ShipColor, Projectile, projectiles, Asteroid, asteroids
)

space_game_entities.configure(settings.ASSETS_PATH)

player = Player((640, 360))          # Standard-Schiff, rot
player = Player((640, 360), ship=ShipType.FIGHTER, color=ShipColor.BLUE, speed=600)  # optional anpassbar

# in der Game Loop:
player.update(delta_time)
projectiles.update(delta_time)
asteroids.update(delta_time)

Asteroid()  # spawnt an zufälliger Position mit zufälliger Größe/Farbe

pygame.sprite.groupcollide(projectiles, asteroids, True, True)
pygame.sprite.spritecollide(player, asteroids, dokill=True)
```

Optional lässt sich sowohl `Player` als auch `Asteroid` an eine `space_game_physics.PhysicsWorld` anbinden
(siehe [Aufgabe 11](../../exercises/exercise-11/README.md)), ohne dass dafür die Klassen selbst angepasst werden müssen:

```python
from space_game_physics import PhysicsWorld

world = PhysicsWorld()
player = Player((640, 360), physics_world=world)
Asteroid(physics_world=world)

# in der Game Loop:
world.step(delta_time)
```

## Bonus: Explosion, Enemy & Asteroiden-Splitting (nur `exercises/showcase`)

Die folgenden Erweiterungen sind rein additiv und ändern nichts am Verhalten der Aufgaben 1-11 - sie werden
ausschließlich vom [Showcase](../../exercises/showcase/README.md) genutzt, der oben auf Aufgabe 11 aufbaut.

**`Asteroid.take_damage(amount=1)`** - Alternative zu `.kill()`: zieht Trefferpunkte ab (BIG=2, MEDIUM=1)
und gibt `True` zurück, sobald der Asteroid dadurch zerstört ist. BIG erzeugt dabei automatisch zwei
MEDIUM-Asteroiden an der eigenen Position, MEDIUM verschwindet endgültig. `.kill()` selbst bleibt
unverändert (kein Splitting) - `pygame.sprite.groupcollide(projectiles, asteroids, True, True)` aus den
Aufgaben 6-11 funktioniert deshalb weiterhin exakt wie bisher.

```python
hits = pygame.sprite.groupcollide(projectiles, asteroids, True, False)
for projectile, hit_asteroids in hits.items():
    for asteroid in hit_asteroids:
        HitExplosion(projectile.rect.center)   # kleiner Effekt bei jedem Treffer
        if asteroid.take_damage():
            Explosion(asteroid.rect.center)    # große Explosion nur beim tatsächlichen Tod
            player.asteroids_destroyed += 1
```

**`Explosion(position)`** / **`HitExplosion(position)`** - Spielen einmalig ihr jeweiliges Sprite-Sheet
(2-fach hochskaliert, siehe `scale` in `_SpriteSheetAnimation`) an einer Position ab und entfernen sich
danach selbst. `Explosion` (`assets/images/asteroid/explosion.png`, 8 Frames, Gruppe `explosions`) ist für
den tatsächlichen Tod eines Objekts gedacht (Asteroid, Enemy, Player), `HitExplosion`
(`assets/images/projectile/hit_explosion.png`, 7 Frames, Gruppe `hit_explosions`) für jeden einzelnen
Treffer, unabhängig davon, ob dabei etwas zerstört wird.

**`Enemy()`** - Gegnerisches Schiff (`assets/images/enemy/`), das oben patrouilliert, Asteroiden ausweicht
und ausschließlich senkrecht nach unten schießt (kein Zielen/Drehen). Um trotzdem treffen zu können,
positioniert es sich stattdessen aktiv horizontal über der aktuellen Spielerposition. Hält mehrere Treffer
aus (`enemy.take_damage()`, analog zu `Asteroid.take_damage()`). Seine Schüsse landen automatisch sowohl in
`projectiles` (zählen z.B. auch gegen Asteroiden) als auch zusätzlich in `enemy_projectiles` - letztere
Gruppe dient **nur** dem Treffer-Check gegen den Spieler, nicht dem Update/Zeichnen (sonst würden diese
Projektile doppelt bewegt).

```python
enemy = Enemy()

# in der Game Loop:
enemies.update(delta_time, player, asteroids)
projectiles.update(delta_time)          # bewegt auch die Schüsse von Enemy mit

# Treffer-Check Spieler <-> Gegner-Schüsse:
pygame.sprite.spritecollide(player, enemy_projectiles, dokill=True)
```

**`Projectile(position, direction=..., color="blue", owner=None)`** - `Projectile` selbst kann jetzt auch in
beliebige Richtungen fliegen und wird passend dazu gedreht (Standard bleibt unverändert: ungedreht nach
oben, blau). `Enemy` nutzt das, um mit `color="red"` nach unten zu schießen, statt eine eigene
Projektil-Klasse zu brauchen. Über `owner` weiß ein Schuss, wer ihn abgefeuert hat - damit lässt sich im
eigenen Kollisions-Code verhindern (siehe Showcase-Lösung), dass ein Schuss sein eigenes Schiff trifft,
solange er direkt nach dem Abschuss noch mit dessen Hitbox überlappt.
