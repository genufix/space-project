# Aufgabe 9 - Menue und Namnesabfrage

Mit diesem Modul möchten wir unserem Spiel ein Menue verpassen.  
Der Spieler bekommt ein echtes Raumschiff, das Projektil sieht aus wie ein Laser und spielt beim Schuss einen Sound ab.  
Der Hintergrund erhält ein Bild und während des Spiels läuft Musik.

> [!note]INFO
>
> Dieses Modul dient lediglich als Anhaltspunkt.    
> Du kannst gerne dein eigenes Hintergrundbild verwenden und das Menue selbst gestalten.

## Vorbereitung: Spieler Namensattribut geben

Bevor wir mit dem Menue  beginnen, sollten wir es ermoeglichen, den Namen vom
Spieler zu speichern.

In Aufgabe 5 haben wir die Spielerklasse implementiert.
Die Klasse besitzt bereits Attribute um zum Beispiel das Raumschiffbild zu speichern.

Fuer das Menue muessen wir unseren game-loop als funktion definieren,
die abgerufen wird, sobald wir auf Spielen druecken.
In diese Funktion wollen wir gleichzeitig den Spielernamen als Parameter uebergeben.

Aufgabe 1: Erweiter die Klasse um das Namensattribut.
Aufgabe 2: Definiere den game-loop als Funktion mit entsprechendem Parameter.

<details>

<summary>

#### Lösung

</summary>

1. Innerhalb `__init__()`:

```diff
    class Player(pygame.sprite.Sprite):
    +    def __init__(self, position, *groups, name):
            # {...}
            self.last_shot = 0
            self.asteroids_destroyed = 0
            self.lives = 3
            self.velocity = 450
            self.direction = pygame.math.Vector2()
+           self.name = name
  ```

1. Innerhalb main.py :
```diff
+ def game(player_name):

    # Clock definieren
    clock = pygame.time.Clock()
    delta_time = 0
    
    # Mixer initialisieren
    pygame.mixer.init()
    # Hintergrund laden
    background = utils.tile_loader.load_background(
        settings.ASSETS_PATH / "images" / "background" / "starfield" / "tile_1.png"
    )
    # background_rect = background.get_rect(center=())
    
    # Sounds laden
    game_music = pygame.mixer.Sound(
        settings.ASSETS_PATH / "music" / "synthwave" / "loop_7.mp3"
    )
    game_music.set_volume(0.5)
    game_music.play(loops=-1, fade_ms=1000)
    
    alarm = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "alarm" / "loop_3.wav")
    alarm.set_volume(0.3)
    
    impact = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "impact" / "blast_1.wav")
    impact.set_volume(0.5)
    
    # Spieler initialisieren
    player = Player((settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2))
    player.name = player_name
    # Asteroid Hilfsvariablen
    last_asteroid_spawn = 0
    asteroid_cooldown = 1000  # in ms
    # Game Loop
    running = True
    while running:
        # Eingaben (Events) abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Zeichenfläche zurücksetzen
        display_surface.blit(background)
        debug(f"Lives: {player.lives}", 10, 10)
        debug(f"Asteroids: {player.asteroids_destroyed}", 10, 40)
    
        # TODO: Hier werden wir unsere Spiellogik implementieren
    
        # Kollision: Projektile <-> Asteroiden
        projectile_asteroid_collisions = pygame.sprite.groupcollide(
            projectiles, asteroids, True, True
        )
        if projectile_asteroid_collisions:
            player.asteroids_destroyed += 1
            impact.play()
    
        # Kollision: Spieler <-> Asteroiden
        if pygame.sprite.spritecollide(player, asteroids, dokill=True):
            player.lives -= 1
            impact.play()
            if player.lives == 0:
                running = False
            elif player.lives == 1:
                alarm.play()
    
        # Sprites updaten
        projectiles.update(delta_time)
        asteroids.update(delta_time)
        player.update(delta_time)
    
        # Asteroiden erzeugen
        current_time = pygame.time.get_ticks()
        if current_time - last_asteroid_spawn >= asteroid_cooldown:
            Asteroid()
            last_asteroid_spawn = current_time
    
        # Projektil(e) auf Display Surface zeichnen
        projectiles.draw(display_surface)
    
        # Asteroid(en) auf Display Surface zeichen
        asteroids.draw(display_surface)
    
        # Spieler auf Display Surface zeichnen
        display_surface.blit(player.image, player.rect)
    
        # Änderungen auf der Zeichenfläche sichtbar machen
        pygame.display.flip()
    
        # Delta Time berechnen (Sekunden seit letztem Frame)
        delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden
    
    # Anwendung sauber beenden
    pygame.quit()


```



</details>

## Schritt 1 - Main Menu importieren
```diff

import pygame
import settings
import utils
from debug import debug
from entity.player import Player
from entity.projectile import projectiles
from entity.asteroid import Asteroid, asteroids
+ from menu import MainMenu
import utils.tile_loader

```

## Schritt 2 - Main Menu aufrufen

```diff
    pygame.quit()



+ MainMenu(game, display_surface).main_menu()

    
```
