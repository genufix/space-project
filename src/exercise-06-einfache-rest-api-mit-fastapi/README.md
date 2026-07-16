# Übung 06: FastAPI Backend erstellen

REST-API für das Space Invaders Scoreboard. Gebaut mit **FastAPI** und **SQLite**.

> [!Tip] Wichtig
Erstmal `database.py` ausführen. Wenn VS-Code geschlossen wird oder ähnliches muss es nochmal ausgeführt werden.
---

## Voraussetzungen

```bash
uv sync
```

## Server starten

```bash
uv run fastapi dev main.py --host 0.0.0.0
```

Der Server läuft danach und hört auf allen Interfaces auf eingehende Anfragen. Unter `http://127.0.0.1:8000` kannst du das am Server direkt testen.

> [!TIP]
> Unter `http://127.0.0.1:8000/docs` steht eine automatisch generierte, interaktive API-Dokumentation zur Verfügung. Alle Endpoints können dort direkt getestet werden.

---

## Konfiguration

### Datenbank

Die Datenbankverbindung wird über `get_db()` aus der datei `database.py` bereitgestellt:

```python
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "space_invaders.db")

def get_db():
    return sqlite3.connect(DB_PATH)
```

Dadurch muss die Datenbank nicht im selben Ordner liegen wie der Ort wo man arbeitet. Das heißt man kann sie von überall aus ansprechen. 

### Score-Berechnung

```python
def calculate_score(asteroids_destroyed: int, time_lived: float) -> int:
    return asteroids_destroyed * 100 + int(time_lived)
```

Der Score wird immer serverseitig berechnet. Negative Werte werden mit einem `ValueError` abgelehnt.

---

## Endpoints

### GET /

Gibt eine Statusmeldung zurück.

**Antwort:**
```json
{"nachricht": "Hallo Welt, mein Backend läuft!"}
```

---

### GET /hallo/{name}

Gibt eine personalisierte Begrüssung zurück.

**URL-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `name` | `string` | Name, der in der Begrüssung erscheint |

**Beispiel:** `GET /hallo/Max`

**Antwort:**
```json
{"nachricht": "Hallo, Max!"}
```

---

### GET /spieler

Gibt alle Spieler aus der Datenbank zurück.

**Antwort:**
```json
[
  {
    "id": 1,
    "name": "Max",
    "device_id": "1bcc5d19-82c9-4b34-b568-b976a47d9062",
    "score": 10180,
    "level": null,
    "datum": "2024-06-10T12:00:00+00:00"
  }
]
```

---

### GET /spieler/{spieler_id}

Gibt einen einzelnen Spieler anhand seiner ID zurück.

**URL-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `spieler_id` | `integer` | ID des Spielers |

**Beispiel:** `GET /spieler/1`

**Antwort bei Erfolg:**
```json
{
  "id": 1,
  "name": "Max",
  "device_id": "1bcc5d19-82c9-4b34-b568-b976a47d9062",
  "score": 10180,
  "level": null,
  "datum": "2024-06-10T12:00:00+00:00"
}
```

**Antwort wenn nicht gefunden:** `404 Not Found`
```json
{"detail": "Spieler nicht gefunden"}
```

---

### POST /spieler

Legt einen neuen Spieler in der Datenbank an. Der initiale Score wird auf `0` gesetzt.

**Query-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `device_id` | `string` | Geraete-ID des Spielers |
| `name` | `string` | Name des Spielers |

**Beispiel:** `POST /spieler?device_id=1bcc5d19-82c9-4b34-b568-b976a47d9062&name=Max`

**Antwort bei Erfolg:** `201 Created`
```json
{
  "id": 1,
  "device_id": "1bcc5d19-82c9-4b34-b568-b976a47d9062",
  "name": "Max",
  "score": 0,
  "level": null,
  "datum": "2024-06-10T12:00:00+00:00"
}
```

**Antwort wenn Spieler bereits existiert:** `409 Conflict`
```json
{"detail": "Spieler existiert bereits"}
```

> [!NOTE]
> Der Existenz-Check prueft, ob `name` **und** `device_id` gleichzeitig bereits in der Datenbank vorhanden sind.

---

### PUT /spieler/{spieler_id}/scores

Aktualisiert den Score eines Spielers. Der neue Score wird aus den Spieldaten berechnet: `asteroids_destroyed x 100 + time_lived`.

**URL-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `spieler_id` | `integer` | ID des Spielers |

**Query-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `asteroids_destroyed` | `integer` | Anzahl abgeschossener Asteroiden |
| `time_lived` | `float` | Ueberlebenszeit in Sekunden |

**Beispiel:** `PUT /spieler/1/scores?asteroids_destroyed=100&time_lived=180.2`

Berechneter Score: `100 x 100 + 180 = 10.180`

**Antwort bei Erfolg:**
```json
{
  "id": 1,
  "name": "Max",
  "device_id": "1bcc5d19-82c9-4b34-b568-b976a47d9062",
  "score": 10180,
  "level": null,
  "datum": "2024-06-10T12:00:00+00:00"
}
```

**Antwort wenn nicht gefunden:** `404 Not Found`
```json
{"detail": "Spieler nicht gefunden"}
```

**Antwort bei negativen Werten:** `400 Bad Request`
```json
{"detail": "Negative Werte sind nicht erlaubt"}
```

---

### GET /scores

Gibt die Spieler sortiert nach Score zurueck (hoechster zuerst).

**Query-Parameter:**

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|--------------|
| `limit` | `integer` | `10` | Maximale Anzahl an Eintraegen |

**Beispiel:** `GET /scores?limit=3`

**Antwort:**
```json
[
  {
    "id": 1,
    "name": "Max",
    "device_id": "1bcc5d19-82c9-4b34-b568-b976a47d9062",
    "score": 10180,
    "level": null,
    "datum": "2024-06-10T12:00:00+00:00"
  }
]
```

---

## Statuscodes

| Code | Bedeutung | Wann |
|------|-----------|------|
| `200` | OK | Anfrage erfolgreich |
| `201` | Created | Neuer Spieler wurde angelegt |
| `400` | Bad Request | Ungueltige Eingabe (z. B. negative Werte) |
| `404` | Not Found | Spieler wurde nicht gefunden |
| `409` | Conflict | Spieler existiert bereits |


---


### Mini-Übung 1: Datenfluss verstehen
Ein Spieler durchläuft in diesem System zwei Schritte: erst POST /spieler, dann PUT /spieler/{id}/scores.
Schau dir an, was POST /spieler beim Anlegen als Score speichert – und wo calculate_score() aufgerufen wird.
Warum wurde das so aufgeteilt statt alles in einem einzigen Endpoint zu erledigen? Was wäre der Nachteil, wenn POST /spieler bereits asteroids_destroyed und time_lived entgegennehmen würde?

### Mini-Übung 2: Der Existenz-Check
In POST /spieler steht dieser Check:
```python
cur.execute(
    "SELECT id FROM players WHERE name = ? AND device_id = ?",
    (name, device_id)
)
```
Der Check nutzt AND – beide Bedingungen müssen gleichzeitig zutreffen.
Was bedeutet das konkret? Könnte sich „AstroAlex" mit einer anderen device_id ein zweites Mal registrieren? Könnte dieselbe device_id mit einem anderen Namen nochmal angelegt werden? Wäre OR hier besser oder schlechter – und warum?

### Mini-Übung 3: Query Parameter vs. Request Body
Der PUT-Endpoint ist so definiert:

```python
def punkte_aendern(spieler_id: int, asteroids_destroyed: int, time_lived: float):
```
Das bedeutet: asteroids_destroyed und time_lived werden als Query Parameter übergeben – also in der URL:
```
PUT /spieler/3/scores?asteroids_destroyed=100&time_lived=180.2
```
Der POST /spieler-Endpoint nimmt seine Daten (`device_id`, `name`) übrigens **ebenfalls** als Query Parameter entgegen – nicht als Request Body.
Was ist der Unterschied zwischen Query Parametern und einem Request Body (JSON) – und welche Probleme könnte es geben, wenn man sensible oder große Datenmengen als Query Parameter statt als Body überträgt?
