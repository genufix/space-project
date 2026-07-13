# space-game-ui

Fertige Start-, Pause- und Death-Screen-Komponenten für das `space-game`-Praktikum, inklusive Menü-Musik
und einem Bestätigungs-Sound für Enter/Q/Esc.

Dieses Package wird nicht selbst geschrieben, sondern in [Aufgabe 10](../../exercises/exercise-10/README.md) fertig
in `game/main.py` eingebunden.

```python
import pygame
import space_game_ui
from space_game_ui import Menu

pygame.mixer.init()  # muss vor Menu() aufgerufen worden sein - Menu lädt eigene Sounds
space_game_ui.configure(settings.ASSETS_PATH)  # einmalig, bevor Menu() erzeugt wird
menu = Menu(display_surface)

player_name = menu.start_screen(background=background)
# ...
if not menu.pause_screen(background=display_surface.copy()):
    running = False
# ...
play_again = menu.death_screen(asteroids_destroyed=5, time_lived=42.3, background=display_surface.copy())
```

* `background` ist bei allen drei Screens optional - ohne Angabe wird ein einfacher dunkler Hintergrund
  gezeichnet, mit Angabe (z. B. der geladene Sternenhimmel oder eine Kopie des aktuellen Spielbilds) wirken
  die Screens wie ein durchgängiger Teil des Spiels statt eines isolierten Overlays.
