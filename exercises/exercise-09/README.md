# Aufgabe 9 - Score an die API senden

Bisher verschwindet unser Highscore einfach, sobald wir das Spiel schließen.  
In diesem Modul lernst du, wie man mit **[httpx](https://www.python-httpx.org/)** HTTP-Requests an eine API sendet,  
damit dein Score dauerhaft gespeichert wird und später z. B. auf einer Highscore-Liste erscheinen kann.

> [!IMPORTANT] Wichtig:
>
> Damit dieses Modul funktioniert, muss eine passende API unter der in `settings.py` konfigurierten Adresse laufen.  
> Falls (noch) keine API erreichbar ist, ist das nicht schlimm. Wir fangen diesen Fall in diesem Modul bewusst ab,  
> damit das Spiel trotzdem ganz normal spielbar bleibt.

## Schritt 1 - Der Ablauf

Bevor wir Code schreiben, schauen wir uns an, was beim Senden eines Scores eigentlich passieren soll:

1. **Geräte-ID ermitteln** - Ein zufälliger, aber dauerhafter Identifier für diesen Rechner (`device_id`)
2. **Spieler anlegen** - Wir senden `device_id` und `name` an die API und erhalten dafür eine eindeutige **Player-ID** zurück
3. **Score senden** - Erst nachdem wir eine Player-ID haben, senden wir `asteroids_destroyed` und `time_lived`, verknüpft mit dieser Player-ID

> [!NOTE] Info:
>
> Warum brauchen wir dafür zwei Requests? Die API kennt zu Beginn nur die `device_id`, aber noch keinen Namen  
> und keinen Score. Erst wenn wir einen Spieler-Datensatz angelegt haben, bekommen wir eine eindeutige ID,  
> unter der der spätere Score gespeichert werden kann.

## Schritt 2 - Eine dauerhafte Geräte-ID erzeugen

Damit man dich auf einer Highscore-Liste wiedererkennt (auch über mehrere Spieldurchläufe hinweg),  
brauchen wir eine ID, die einmalig erzeugt und danach lokal gespeichert wird.

Python liefert dafür das Modul [`uuid`](https://docs.python.org/3/library/uuid.html), mit dem wir uns  
eine praktisch garantiert einzigartige ID erzeugen lassen können. Würden wir bei jedem Programmstart aber  
eine neue `device_id` erzeugen, könnten wir dich nie wiedererkennen. Eine ID einmalig zu erzeugen und danach  
lokal in einer Datei zu lesen/schreiben hat aber wenig mit Spieleentwicklung zu tun. Deshalb bekommst du dafür  
genau wie `debug()`, `load_background()` und `ApiClient` die fertige Funktion `get_device_id()` aus dem Package  
`space-game-utils`.

```python
from space_game_utils import get_device_id

device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")
```

> [!NOTE] Info:
>
> Existiert die angegebene Datei bereits, liest `get_device_id()` die gespeicherte ID einfach wieder ein.  
> Falls nicht, erzeugt sie eine neue ID und schreibt sie in die Datei, damit sie beim nächsten Start wieder  
> verfügbar ist. Der Pfad zeigt bewusst **neben** `assets/` auf den Projekt-Root, nicht in `assets/` selbst -  
> `device_id.txt` ist ja keine Bild-, Sound- oder Musikdatei.

## Schritt 3 - Die API-Adresse konfigurieren

Wie den `ASSETS_PATH` wollen wir auch die Adresse unserer API zentral in `settings.py` verwalten:

```python
# API Adresse
API_BASE_URL = "http://localhost:8000"
```

## Schritt 4 - Der fertige API-Client

Für die beiden Requests (Spieler anlegen, Score senden) bräuchten wir eine kleine Hilfsklasse, die  
[`httpx`](https://www.python-httpx.org/) (eine moderne Bibliothek für HTTP-Requests in Python) verwendet.  
Eine HTTP-Client-Klasse mit Fehlerbehandlung von Grund auf selbst zu entwerfen, hat aber wenig mit  
Spieleentwicklung zu tun - deshalb bekommst du sie, genau wie `debug()` und `load_background()`, bereits fertig  
aus dem Package `space-game-utils`: `ApiClient`.

> [!NOTE] Info:
>
> Die API stellt dafür folgende zwei Endpunkte bereit:
>
> | Methode | Endpunkt               | Body (JSON)                                                           | Antwort (JSON)   |
> | ------- | ---------------------- | --------------------------------------------------------------------- | ---------------- |
> | `POST`  | `/spieler`             | `{"device_id": str, "name": str}`                                     | `{"id": int}`    |
> | `PUT`   | `/spieler/{id}/scores` | `{"player_id": int, "asteroids_destroyed": int, "time_lived": float}` | `{"id": int}`    |

`packages/space-game-utils/src/space_game_utils/api.py` (zum Nachlesen, nicht selbst schreiben):

```python
import httpx


class ApiClient:
    """Kleiner HTTP-Client für die Score-API (siehe Aufgabe 9)."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_player(self, device_id: str, name: str) -> int:
        """Registriert den Spieler bei der API und gibt seine Spieler-ID zurück."""
        response = httpx.post(
            f"{self.base_url}/spieler",
            params={"device_id": device_id, "name": name},
        )
        response.raise_for_status()
        return response.json()["id"]

    def submit_score(
        self, player_id: int, asteroids_destroyed: int, time_lived: float
    ) -> None:
        """Meldet einen Score für die übergebene Spieler-ID an die API."""
        response = httpx.put(
            f"{self.base_url}/spieler/{player_id}/scores",
            params={
                "player_id": player_id,
                "asteroids_destroyed": asteroids_destroyed,
                "time_lived": time_lived,
            },
        )
        response.raise_for_status()
```

> [!NOTE] Info:
>
> `response.raise_for_status()` wirft einen Fehler, falls die API mit einem Fehlercode (z. B. `404` oder `500`) antwortet.  
> So merken wir sofort, wenn etwas nicht wie erwartet funktioniert, statt einfach mit einer leeren Antwort weiterzumachen.  
> Du musst diese Datei nicht selbst schreiben. Wichtig ist nur, dass du `create_player()` und `submit_score()`  
> gleich richtig aufrufst.

## Schritt 5 - Spieler beim Start anlegen

Bevor die Game Loop beginnt, fragen wir den Namen des Spielers ab und legen ihn über die API an.

> [!NOTE] Info:
>
> Aktuell fragen wir den Namen einfach über die Konsole mit `input()` ab.  
> Sobald wir ein eigenes Start-Menü haben, wird diese Eingabe durch ein Textfeld ersetzt.

Ergänze in `main.py` (das `import httpx` brauchen wir gleich, um Fehler abzufangen):

```python
import httpx
from space_game_utils import get_device_id, ApiClient

# {...}

api_client = ApiClient(settings.API_BASE_URL)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")
player_name = input("Wie lautet dein Name? ")

try:
    player_id = api_client.create_player(device_id, player_name)
except httpx.HTTPError:
    print("Konnte keine Verbindung zur API aufbauen. Der Score wird nicht gespeichert.")
    player_id = None
```

> [!IMPORTANT] Wichtig:
>
> `httpx.HTTPError` ist die gemeinsame Oberklasse für **beide** Fehlerarten, die hier auftreten können:  
> `httpx.RequestError` bei Netzwerkproblemen (z. B. weil die API gar nicht läuft) und `httpx.HTTPStatusError`,  
> wenn die API zwar antwortet, aber mit einem Fehlercode (den wirft `raise_for_status()` im `ApiClient`).  
> Würden wir nur `httpx.RequestError` abfangen, würde eine erreichbare, aber fehlerhafte API unser Spiel crashen.  
> Ist `player_id` anschließend `None`, wissen wir, dass wir später keinen Score senden können - das Spiel läuft aber trotzdem ganz normal weiter.

> [!TIP] Tipp:
>
> **▶ Führe das Spiel jetzt aus:** Gib beim Start einen Namen ein - läuft eine API unter `API_BASE_URL`, sollte  
> im Terminal kein Fehler erscheinen. Läuft keine, siehst du die Fehlermeldung, das Spiel bleibt aber spielbar.

## Schritt 6 - Score senden, wenn der Spieler stirbt

Sobald der Spieler keine Leben mehr hat, kennen wir bereits `player.asteroids_destroyed`.  
Die Zeit, die er überlebt hat, berechnen wir bereits jeden Frame in der Variable `time_lived` fürs HUD  
(siehe [Aufgabe 7](../exercise-07/README.md)) - die können wir hier einfach weiterverwenden.

<details>
<summary>

#### Lösung

</summary>

```diff
    # Kollision: Spieler <-> Asteroiden
    if pygame.sprite.spritecollide(player, asteroids, dokill=True):
        player.lives -= 1
        impact.play()
        if player.lives == 0:
            running = False
+
+           if player_id is not None:
+               try:
+                   api_client.submit_score(
+                       player_id, player.asteroids_destroyed, time_lived
+                   )
+               except httpx.HTTPError:
+                   print("Score konnte nicht gesendet werden.")
        elif player.lives == 1:
            alarm.play()
```

</details>

> [!TIP] Tipp:
>
> **▶ Führe das Spiel jetzt aus:** Verliere alle Leben - läuft eine API, sollte dein Score jetzt dauerhaft  
> gespeichert werden.
