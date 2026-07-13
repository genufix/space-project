# Aufgabe 8 - Texturen, Sounds & Musik

Mit diesem Modul möchten wir unserem Spiel durch Assets mehr Leben einhauchen.  
Der Spieler bekommt ein echtes Raumschiff, das Projektil sieht aus wie ein Laser und spielt beim Schuss einen Sound ab.  
Der Hintergrund erhält ein Bild und während des Spiels läuft Musik.

> [!note]INFO
>
> Dieses Modul dient lediglich als Anhaltspunkt.    
> Du kannst gerne andere Sounds und Texturen verwenden!

## Vorbereitung: Spielerbewegung verbessern

Bevor wir mit den Assets beginnen, sollten wir die Bewegung des Spielers anpassen.  
In Aufgabe 6 haben wir gelernt, wie man Richtungsvektoren normalisiert.

Wenn man sich aktuell diagonal bewegt, z.B. mit `S` und `D` gleichzeitig, bewegt man sich mit dem Vektor `(1, 1)`.  
Das entspricht einer Länge von ca. `1.4`.  
Dadurch ist diagonale schneller als die horizontale und vertikale Bewegung.

Versuch das Problem durch einen Richtungsvektor `self.direction` mit Normalisierung zu beheben und lege fuer die Geschwindigkeit `self.velocity` an.  
Die Bewegungsgeschwindigkeit reduzieren wir dabei von `600` auf `450`.

<details>
<summary>

#### Lösung

</summary>

1. Innerhalb `__init__()`:

    ```diff
    class Player(pygame.sprite.Sprite):
        def __init__(self, position, *groups):
            # {...}
            self.last_shot = 0
            self.asteroids_destroyed = 0
            self.lives = 3
    +         self.velocity = 450
    +         self.direction = pygame.math.Vector2()
    ```

2. Und in `update()`:

    ```diff
        def update(self, delta_time):
            # {...}
    +        # Bewegungsvektor zurecksetzen
    +        self.direction = self.direction.update(0, 0)
            # Tasten-Abfrage, um Spieler zu bewegen
            if keys[pygame.K_w]:
    -             self.rect.y -= 600 * delta_time
    +             self.direction.y -= 1
            if keys[pygame.K_s]:
    -             self.rect.y += 600 * delta_time
    +             self.direction.y += 1
            if keys[pygame.K_a]:
    -             self.rect.x -= 600 * delta_time
    +             self.direction.x -= 1
            if keys[pygame.K_d]:
    -             self.rect.x += 600 * delta_time
    +             self.direction.x += 1

    +         if self.direction.length() > 1:
    +             self.direction = self.direction.normalize()

    +         self.rect.center += self.direction * self.velocity * delta_time
            # {...}
    ```

</details>

## Schritt 1 - Texturen laden

Mit `pygame.image.load()` können wir Bilddateien einfach als Surface laden.  
Diese Surface ersetzt z. B. unsere alte gefärbte Fläche `pygame.Surface((200, 200))`.

Da alle Assets in einem zentralen Ordner liegen, definieren wir in `settings.py` einen praktischen Pfad,  
welchen wir überall wiederverwenden können:

`settings.py`

```python
from pathlib import Path

# Assets Pfad
ASSETS_PATH = Path(__file__).joinpath("..", "..", "assets").resolve()
```

> [!note]INFO
>
> * `__file__`: Gibt uns den Pfad zur aktuellen Datei (`settings.py`)
> * `Path(__file__)`: Erstellt ein Path-Objekt mit dem Pfad zur Datei (`/home/<user>/space-game/src/exercise-08/settings.py`)  
> * `.joinpath("..", "..", "assets")`: Verbindet Pfade (`/home/<user>/space-game/src/exercise-08/settings.py/../../assets`) 
> `.resolve()`: Wandelt den Pfad in einen absoluten Pfad, der betriebssystemunabhängig korrekt ist  
> Das Ergebnis ist z. B. `/home/<user>/space-game/assets`  
> 
> Der Vorteil von `pathlib.Path` ist: Es ist plattformunabhängig (Windows, Linux, Mac) und deutlich lesbarer als `os.path`.

## Schritt 2 - Textur für den Spieler hinzufügen

Versuche das ganze mal innerhalb der `Player`-Klasse zu implementieren:

<details>
<summary>

#### Lösung

</summary>

`entity/player.py`

```diff
  class Player(pygame.sprite.Sprite):
      def __init__(self, position, *groups):
          super().__init__(*groups)

-         self.image = pygame.Surface((200, 200))
-         self.image.fill((125, 55, 240))
+         self.image = pygame.image.load(
+             settings.ASSETS_PATH / "images" / "ship" / "classic" / "red.png"
+         ).convert_alpha()
          self.rect = self.image.get_frect(center=position)
          # {...}
```

> [!note]INFO
>
> `.convert_alpha()`: Diese Methode wandelt das Bild in ein Format um, das schneller auf dem Bildschirm dargestellt werden kann, inklusive Transparenz.  
> Ohne `.convert_alpha()` könnten Bildteile (z. B. der Hintergrund um das Schiff) einen sichtbaren schwarzen oder weißen Rand zeigen.  
> Falls du ein Bild ohne Transparenz lädst (z. B. einen Hintergrund), solltest du stattdessen `.convert()` verwenden.

</details>

## Schritt 3 - Textur für Projektil und Asteroid implementieren

Du kannst das gleiche Vorgehen jetzt für die `Projectile` sowie `Asteroid`-Klasse anwenden.

<details>
<summary>

#### Lösung

</summary>

`entity/projectile.py`

```diff
  class Projectile(pygame.sprite.Sprite):
      def __init__(self, spawn_position, *groups):
          super().__init__(*groups)

-         self.image = pygame.Surface((10, 40))
+         self.image = pygame.image.load(
+             settings.ASSETS_PATH / "images" / "projectile" / "red" / "laser_6.png"
+         )
          self.rect = self.image.get_frect(midbottom=spawn_position)
          # {...}
```

`entity/asteroid.py`

```diff
  class Asteroid(pygame.sprite.Sprite):
      def __init__(self, *groups):
          super().__init__(*groups)

          # Zufällige Position
          x = randint(0, settings.WINDOW_WIDTH)
          y = randint(-300, -80)

-         self.image = pygame.Surface((80, 80))
+         self.image = pygame.image.load(
+             settings.ASSETS_PATH / "images" / "asteroid" / "grey" / "big_1.png"
+         )
          self.rect = self.image.get_frect(center=(x, y))
          # {...}
```

</details>

## Schritt 4 - Hintergrundbild hinzufügen

Unsere Anwendung wirkt langsam deutlich mehr wie ein Spiel, aber der weisse Hintergrund  
liefert noch kein "Weltraum-Feeling".  
Aendere hierfuer innerhalb `main.py` den Hintergrund unseres Spiels.  
Passende Hintergruende findest du in `images/background`.

```python
background = pygame.image.load(
    settings.ASSETS_PATH / "images/background/blue.png"
).convert()  # kein alpha nötig

# im Hauptloop:
screen.blit(background, (0, 0))
```

## Schritt 5 - Sounds und Musik enbauen

Unser Spiel sieht jetzt schon richtig gut aus, aber was wäre ein Weltraumspiel ohne Laser-Sounds mit passender Musik?  
Zwar würde man im Weltall physikalisch keine Geräusche hören, aber für das Spielerlebnis ignorieren wir das mal.

#### Mixer initialisieren

Damit Pygame überhaupt Sounds abspielen kann, müssen wir in main.py zusätzlich zum normalen pygame.init() auch den Mixer starten:

```python
pygame.mixer.init()
```

> [!note] INFO
>
> `pygame.mixer.init()` initialisiert das Audio-System von Pygame.  
> Ohne diesen Schritt funktionieren Methoden wie `pygame.mixer.Sound()` oder `pygame.mixer.music.play()` nicht und führen zu einem Fehler.  
> Dieser Aufruf muss nur einmalig zu Beginn erfolgen, typischerweise direkt nach `pygame.init()`.

## Schritt 6 - Hintergrundmusik einfügen

Jetzt laden wir eine Musikdatei und lassen sie im Hintergrund spielen:

```python
game_music = pygame.mixer.Sound(
    settings.ASSETS_PATH / "music" / "synthwave" / "loop_7.mp3"
)
game_music.set_volume(0.5)
game_music.play(loops=-1, fade_ms=1000)
```

> [!note] INFO
>
> `set_volume(0.5)`: Setzt die Lautstärke der Musik auf `0.5` (akzeptiert Werte zwischen `0.0` und `1.0`)  
> `loops=-1`: Bedeutet, dass die Musik endlos wiederholt werden soll

## Schritt 7 - Schusssound für den Laser

In der `Player`-Klasse können wir beim Schießen einen Soundeffekt abspielen.
Lade den Sound einmal in `__init__()`:

<details>
<summary>

#### Lösung

</summary>

```diff
  class Player(pygame.sprite.Sprite):
      def __init__(self, position, *groups):
          # {...}
+         self.projectile_sound = pygame.mixer.Sound(
+             settings.ASSETS_PATH / "sounds" / "laser" / "bullet_2.wav"
+         )
+         self.projectile_sound.set_volume(0.2)
```

```diff
      def update(self, delta_time):
          # Tasten-Abfrage, um Projektil zu erstellen
          if keys[pygame.K_SPACE]:
              current_time = pygame.time.get_ticks()  # in ms

              if current_time - self.last_shot >= 500:
                  Projectile(self.rect.midtop)
+                 self.projectile_sound.play()
                  self.last_shot = current_time
```

</details>

## Schritt 8 - Kollisionssound, wenn Laser einen Asteroid trifft

Damit wir auch ein Feedback erhalten, wenn wir einen Asteroiden getroffen haben, sollte hierfuer auch ein passender Sound abgespielt werden.  
Da wir ja innerhalb der `main.py` schon abfragen, ob ein Projektil mit einem Asteroid kollidiert, so koennen wir diese Aenderung dort implementieren.

## Bonus: Schadensanzeige ueber Overlays

Wir können auch optisch darstellen, wie beschädigt das Raumschiff ist.
Dazu legen wir verschiedene Damage-Texturen als Overlays über das Schiff.

```python
self.hull = pygame.image.load(
    settings.ASSETS_PATH / "images" / "ship" / "playerShip3_red.png"
).convert_alpha()

self.damage_overlays = {
    3: pygame.image.load(settings.ASSETS_PATH / "images" / "damage" / "damage1.png").convert_alpha(),
    2: pygame.image.load(settings.ASSETS_PATH / "images" / "damage" / "damage2.png").convert_alpha(),
    1: pygame.image.load(settings.ASSETS_PATH / "images" / "damage" / "damage3.png").convert_alpha(),
}
self.prev_lives = self.lives

# Anfangsbild setzen
self.image = pygame.Surface(self.hull.get_size(), pygame.SRCALPHA)
self.image.blit(self.hull, (0, 0))
```
