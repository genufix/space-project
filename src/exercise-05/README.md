# Aufgabe 5 - Die Player-Klasse

In diesem Modul fassen wir den bisherigen Code rund um das Quadrat zusammen und überführen ihn in eine **eigene Klasse**.  
Außerdem lernen wir ein zentrales Feature von pygame kennen: die **Sprite-Klasse**.  
Das macht unseren Code **übersichtlicher** und schafft die Grundlage für spätere Features wie **Gruppen**, **Kollisionen** und **Animationen** von Objekten.

## Schritt 1 - Was ist ein Sprite?

Ein Sprite ist in pygame ein Objekt, das **Grafik und Logik** kombiniert.  
Es stellt Attribute wie `image` und `rect` sowie eine `update()`-Methode zur Verfügung.  
Dazu lassen sich Sprites in sogenannte Gruppen verwalten.  
Sie ermöglichen uns, mehrere Objekte gleichzeitig zu zeichnen, updaten oder auf Kollissionen zu prüfen.

#### Vorteile von Sprites

* Kapseln Aussehen und Verhalten eines Objekts
* Bieten `update()`-Methoden für Bewegung und Logik
* Können in Gruppen organisiert werden (z.B. Projektile, Asteroiden, etc.)
* Erlauben einfache Kollisionserkennung zwischen Sprites

## Schritt 2 - Player-Klasse erstellen

Wir bauen eine eigene Klasse `Player`, die von `pygame.sprite.Sprite` erbt.  
In dieser Klasse lagern wir alle bisherigen Eigenschaften (`Image`, `FRect`, `Bewegung`) unseres Quadrats aus.

`entity/player.py`

```python
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups):

        self.image = pygame.Surface((200, 200))
        self.image.fill((125, 55, 240))

        self.rect = self.image.get_frect(center=position)

    def update(self):
        pass
```

> [!note]INFO
>
> Statt `square` und `square_rect` brauchen wir später nur noch `player.image` und `player.rect`!  
> Weitere Informationen zur **Sprite-Klasse** findest du in der [offiziellen Doku](https://pyga.me/docs/ref/sprite.html#pygame.sprite.Sprite).

## Schritt 3 - Bewegung in `update()` auslagern

**Sprites** haben eine eingebaute `update()`-Methode, die regelmäßig aufgerufen werden kann.  
Darin platzieren wir jetzt die Bewegung `WASD` des Quadrats.

`enity/player.py`

```python
import pygame

class Player(pygame.sprite.Sprite):
    # {...}
    def update(self, delta_time):
        # Liste aller Tasten (gedrückt / nicht gedrückt)
        keys = pygame.key.get_pressed()

        # Tasten-Abfrage, um Spieler zu bewegen
        if keys[pygame.K_w]:
            self.rect.y -= 600 * delta_time
        if keys[pygame.K_s]:
            self.rect.y += 600 * delta_time
        if keys[pygame.K_a]:
            self.rect.x -= 600 * delta_time
        if keys[pygame.K_d]:
            self.rect.x += 600 * delta_time
```

#### Als nächstes räumen wir ungenutzten, alten Code aus:

1. Oberhalb, in der `main.py`:

    ```diff
      import pygame
    + from entity.player import Player

      # {...}
    - # Quadrat definieren
    - square = pygame.Surface((200, 200))
    - square.fill((125, 55, 240))
    - square_rect = square.get_frect()
    - square_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    + # Spieler initialisieren
    + player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    ```

2. Innerhalb der Game Loop:

    ```diff
    - # Liste aller Tasten (gedrückt / nicht gedrückt)
    - keys = pygame.key.get_pressed()
    - 
    - # Tasten-Abfrage, um Quadrat zu bewegen
    - if keys[pygame.K_w]:
    -     square_rect.y -= 600 * delta_time
    - if keys[pygame.K_s]:
    -     square_rect.y += 600 * delta_time
    - if keys[pygame.K_a]:
    -     square_rect.x -= 600 * delta_time
    - if keys[pygame.K_d]:
    -     square_rect.x += 600 * delta_time
    + player.update(delta_time)
    ```

3. Beim Zeichnen:

    ```diff
    - # Quadrat auf Display Surface zeichnen
    - display_surface.blit(square, square_rect)
    + # Spieler auf Display Surface zeichnen
    + display_surface.blit(player.image, player.rect)
    ```

## Schritt 4 - Projektilabschuss in Player auslagern

Auch das Erstellen und Verwalten von Projektilen gehört in die `Player`-Klasse,
dennoch ist es sinnvoll, die Projektile auch in eine eigene Klasse auszulagern.  
Dadurch erbt `Projectile` von Sprite und kann einer Gruppe hinzugefügt werden.  
Wie oben schon erwähnt benötigt man Gruppen, um darin existierende Sprites
zu zeichnen, zu updaten oder um Kollisionen mit anderen Sprites (z.B. Asteroiden) zu ermöglichen.

> [!note]INFO
>
> Gruppen stellen uns nützliche Methoden wie `update()` und `draw()` zur Verfügung.  
> Alle weiteren Details findest du in der [offiziellen Doku](https://pyga.me/docs/ref/sprite.html#pygame.sprite.Group).

`entity/projectile.py`

```python
import pygame

projectiles = pygame.sprite.Group()  # speichert alle aktiven Projectile-Sprites


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups):

        self.image = pygame.Surface((10, 40))
        self.rect = self.image.get_frect(midbottom=position)

        self.add(projectiles)

    def update(self):
        self.rect.y -= 800 * delta_time
```

Versuche unsere bestehende Projektillogik, also den Teil mit der Tastenabfrage `K_SPACE` mit Cooldown, innerhalb der `update()`-Methode der **Player-Klasse** zu implementieren:

> [!note]INFO
>
> Damit du die **Projectile-Klasse** überhaupt ansprechen kannst, müssen wir diese erst mit einem **import-Statement**  
> innerhalb `player.py` verfügbar machen. Schreibe dazu unterhalb von `import pygame` noch `from entity.projectile import Projectile`.

<details>
<summary>

#### Lösung

</summary>

`entity/player.py`

```diff
  class Player(pygame.sprite.Sprite):
      def __init__(self, position, *groups):
          # {...}
+         self.last_shot = 0
  
      def update(self, delta_time):
          # Liste aller Tasten (gedrückt / nicht gedrückt)
          keys = pygame.key.get_pressed()
  
          # Tasten-Abfrage, um Spieler zu bewegen
          # {...}
  
+         # Tasten-Abfrage, um Projektil zu erstellen
+         if keys[pygame.K_SPACE]:
+             current_time = pygame.time.get_ticks()  # in ms
+ 
+             if current_time - self.last_shot >= 500:
+                 Projectile(self.rect.midtop)
+                 self.last_shot = current_time
```

#### Als nächstes müssen wir die bestehende Logik mit der neuen austauschen:

1. Oberhalb, in der `main.py`:

    ```diff
      import pygame
      from entity.player import Player
    + from entity.projectile import projectiles
      # {...}

    - # Projektil definieren
    - projectile = pygame.Surface((10, 40))
    - projectile_rects = []
    - last_shot = pygame.time.get_ticks()  # in ms
    ```

2. Innerhalb der Game Loop:

    ```diff
      # TODO: Hier werden wir unsere Spiellogik implementieren
    + projectiles.update(delta_time)
      player.update(delta_time)

    - # Tasten-Abfrage, um Projektil zu erstellen
    - if keys[pygame.K_SPACE]:
    -     current_time = pygame.time.get_ticks()  # in ms
    - 
    -     if current_time - last_shot >= 500:
    -         temp = projectile.get_frect(midbottom=(square_rect.midtop))
    -         projectile_rects.append(temp)
    -         last_shot = current_time
    
    # Projektil(e) auf Display Surface zeichnen
    - for projectile_rect in projectile_rects:
    -     display_surface.blit(projectile, projectile_rect)
    -     projectile_rect.y -= 800 * delta_time
    + projectiles.draw(display_surface)
    ```

</details>

## Kompletter Code

<details>
<summary>

#### Anzeigen

</summary>

`main.py`

```python
import pygame
from entity.player import Player
from entity.projectile import projectiles

# Grundlegendes Setup
pygame.init()

# Fenstergröße festlegen und Fenster erstellen
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Fenstertitel setzen
pygame.display.set_caption("Space Shooter")

# Framerate und Clock definieren
clock = pygame.time.Clock()
FRAMERATE = 60
delta_time = 0

# Spieler initialisieren
player = Player((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Game Loop
running = True
while running:
    # Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Zeichenfläche zurücksetzen
    display_surface.fill("white")

    # TODO: Hier werden wir unsere Spiellogik implementieren
    projectiles.update(delta_time)
    player.update(delta_time)

    # Projektil(e) auf Display Surface zeichnen
    projectiles.draw(display_surface)

    # Spieler auf Display Surface zeichnen
    display_surface.blit(player.image, player.rect)

    # Änderungen auf der Zeichenfläche sichtbar machen
    pygame.display.flip()

    # Delta Time berechnen (Sekunden seit letztem Frame)
    delta_time = clock.tick(FRAMERATE) / 1000  # ms -> Sekunden

# Anwendung sauber beenden
pygame.quit()
```


`entity/player.py`

```python
import pygame
from entity.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface((200, 200))
        self.image.fill((125, 55, 240))
        self.rect = self.image.get_frect(center=position)

        self.last_shot = 0

    def update(self, delta_time):
        # Liste aller Tasten (gedrückt / nicht gedrückt)
        keys = pygame.key.get_pressed()

        # Tasten-Abfrage, um Spieler zu bewegen
        if keys[pygame.K_w]:
            self.rect.y -= 600 * delta_time
        if keys[pygame.K_s]:
            self.rect.y += 600 * delta_time
        if keys[pygame.K_a]:
            self.rect.x -= 600 * delta_time
        if keys[pygame.K_d]:
            self.rect.x += 600 * delta_time

        # Tasten-Abfrage, um Projektil zu erstellen
        if keys[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()  # in ms

            if current_time - self.last_shot >= 500:
                Projectile(self.rect.midtop)
                self.last_shot = current_time
```


`entity/projectile.py`

```python
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
```

</details>
