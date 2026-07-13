# space-game-utils

Fertige Hilfsfunktionen für das `space-game`-Praktikum, die wenig mit Spielelogik zu tun haben und deshalb
nicht selbst geschrieben werden: Debug-Text auf dem Bildschirm, ein HUD (Leben/Score/Zeit), ein kachelbarer
Hintergrund, eine dauerhafte Geräte-ID und ein kleiner HTTP-Client für die Score-API.

```python
import space_game_utils
from space_game_utils import debug, draw_hud, load_background, get_device_id, ApiClient

# Einmalig beim Start: Assets-Pfad setzen (wird u.a. für den HUD-Font gebraucht)
space_game_utils.configure(settings.ASSETS_PATH)

# Einzelne Werte während der Entwicklung anzeigen (Aufgabe 7)
debug(f"Lives: {player.lives}")

# HUD mit Herz-Slots, zerstörten Asteroiden und Zeit zeichnen (Aufgabe 7)
draw_hud(player.lives, player.asteroids_destroyed, time_lived)

# Einzelnes Tile-Bild zu einem bildschirmfüllenden Hintergrund kacheln (Aufgabe 8)
background = load_background(settings.ASSETS_PATH / "images" / "background" / "starfield" / "tile_1.png")

# Dauerhafte Geräte-ID lesen/erzeugen & Score-API ansprechen (Aufgabe 9)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")
api_client = ApiClient(settings.API_BASE_URL)
player_id = api_client.create_player(device_id, player_name)
api_client.submit_score(player_id, player.asteroids_destroyed, time_lived)
```

* `configure(assets_path)`: Muss einmalig beim Programmstart aufgerufen werden, bevor `draw_hud()` verwendet
  wird - sagt dem Package, wo der `assets/`-Ordner liegt
* `debug(text, x=10, y=10)`: Schreibt `text` an eine beliebige Bildschirmposition - praktisch zum schnellen
  Testen von Werten während der Entwicklung (siehe [Aufgabe 7](../../exercises/exercise-07/README.md))
* `draw_hud(lives, asteroids_destroyed, time_lived, max_lives=4)`: Zeichnet das HUD (Herz-Slots, Anzahl
  zerstörter Asteroiden, Zeit) oben auf den Bildschirm (siehe [Aufgabe 7](../../exercises/exercise-07/README.md))
* `load_background(path)`: Kachelt ein einzelnes Hintergrund-Tile zu einer bildschirmfüllenden `Surface`
  (siehe [Aufgabe 8](../../exercises/exercise-08/README.md))
* `get_device_id(path)`: Liest die dauerhafte Geräte-ID aus `path`, oder erzeugt und speichert eine neue,
  falls die Datei noch nicht existiert (siehe [Aufgabe 9](../../exercises/exercise-09/README.md))
* `ApiClient(base_url)`: Legt Spieler an (`create_player`) und sendet Scores (`submit_score`) an die API
  (siehe [Aufgabe 9](../../exercises/exercise-09/README.md))
