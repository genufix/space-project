# Übung 04: Python und Datenbank verbinden

> [!note] Lernziel:
> Das ist der Moment, wo alles zusammenkommt! Du weißt jetzt, wie SQL funktioniert. Du weißt, wie man Python-Skripte schreibt. Jetzt kombinieren wir beides – Python spricht mit der Datenbank, ganz automatisch!

> [!Tip] Wichtig
Erstmal `database.py` ausführen. Wenn VS-Code geschlossen wird oder ähnliches muss es nochmal ausgeführt werden.


Python hat ein eingebautes Modul namens `sqlite3`, was wir direkt nutzen können!

Das Grundprinzip funktioniert immer nach demselben Schema:
1. Verbindung zur Datenbank herstellen
2. Einen „Cursor" erstellen (das Werkzeug, das SQL-Befehle ausführt)
3. SQL-Befehl ausführen
4. Änderungen speichern (`commit`) – bei INSERT, UPDATE, DELETE
5. Verbindung schließen (Nur relevant wenn man "with" nicht benutzt) 

Mehr Informationen gibt es in der [Python Dokumentation - SQLite3](https://docs.python.org/3/library/sqlite3.html).


## 1. Tabelle erstellen mit Python

Erstelle `datenbank_setup.py`:

```python
from database import get_db


with get_db() as conn:
    cursor = conn.cursor()

    # Tabelle erstellen (falls sie noch nicht existiert)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT    NOT NULL,
            device_id   TEXT,
            score       INTEGER DEFAULT 0,
            level       INTEGER,
            datum       TEXT
        )
    """)

    # Änderungen dauerhaft speichern
    conn.commit()
    print("✅ Datenbank ist bereit!")
```

Führe es aus:
```bash
uv run datenbank_setup.py
```

> [!tip] 'CREATE TABLE IF NOT EXISTS'
> Dieser Zusatz verhindert, dass eine Tabelle erstellt wird, die schon existiert. Mit anderen Worten, falls eine Tabelle mit dem gewählten Namen bereits exisitert, dann wird die Erstellung derselben bzw. einer weiteren Tabelle verhindert.

---

## 2. Daten einfügen – sicher mit Platzhaltern

Erstelle `score_einfuegen.py`:

```python
import sys, os
from datetime import date
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from database import get_db


def score_speichern(name, device_id, score, level):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO players (name, device_id, score, level, datum)
            VALUES (?, ?, ?, ?, ?)
        """, (name, device_id, score, level, str(date.today())))

        conn.commit()
        print(f"✅ Score von {name} ({score} Punkte) gespeichert!")

# Funktion aufrufen
score_speichern("AstroAlex", "badb7dc2-ad9a-4c8e-a96d-591f707bd5ed", 42000, 5)
score_speichern("GalaxyGreta", "3e3d1123-36f9-4237-a058-77b4f314475f", 38500, 3)
score_speichern("NebulaNiko", "9a1d0240-13ab-477c-a22a-3ac33d223fa7", 51200, 7)
```

> [!Warning] Achtung: Warum die Fragezeichen '?'
> Statt die Werte direkt in den SQL-String einzubauen, nutzen wir `?` als Platzhalter.
> **Warum?** Sicherheit! Wenn jemand als Spielernamen `"; DROP TABLE players; --"` eingibt, würde direktes Einfügen die Datenbank löschen. Das nennt sich **SQL Injection** – ein echter Angriff im Internet. Die `?`-Methode schützt davor automatisch, weil Python den Wert sicher verarbeitet.

---

## 3. Das `sqlite3`-Modul

```python
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from database import get_db

# 1. Verbindung herstellen (Datei wird erstellt, falls sie nicht existiert)
with get_db() as conn:

    # 2. Cursor erstellen
    cursor = conn.cursor()

    # 3. SQL-Befehl ausführen
    cursor.execute("SELECT * FROM players")

    # 4. Ergebnisse abrufen
    ergebnisse = cursor.fetchall()
    print(ergebnisse)

    # Man muss nicht die Verbindung selber schließen weil das 'with' macht
```

> [!note] Was ist ein Cursor?
> Stell dir den Cursor wie einen Zeiger in einem Buch vor – er markiert, an welcher Stelle du gerade arbeitest. Alle SQL-Befehle werden über den Cursor ausgeführt. Der Cursor ist das Werkzeug, die Verbindung ist die Tür zur Datenbank.

---



## 4. Daten lesen und anzeigen

Erstelle `scores_anzeigen.py`:

```python
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from database import get_db

def alle_scores_anzeigen():
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM players ORDER BY score DESC")
        eintraege = cursor.fetchall()

        print("\n🏆 SPACE INVADERS HIGHSCORES 🏆")
        print("-" * 45)

        for platz, eintrag in enumerate(eintraege, start=1):
            id, name, device_id, score, level, datum = eintrag
            print(f"  {platz}. {name:<15} {score:>8} Punkte  (Level {level})")

        print("-" * 45)

alle_scores_anzeigen()
```

> [!tip] fetchall() vs fetchone()
> `cursor.fetchall()` → gibt alle Ergebniszeilen als Liste zurück
> `cursor.fetchone()` → gibt nur die erste Zeile zurück – praktisch, wenn du z. B. nur den Highscore willst

---

## Mini-Übung 1: Score aktualisieren

Schreibe eine Funktion `score_aktualisieren(name, neuer_score)`, die den Score eines Spielers in der Datenbank ändert.

Teste sie: Gib AstroAlex 99999 Punkte – er hat sich das verdient! 🚀

> [!tip] Tipp
> Du brauchst ein `UPDATE ... SET score = ? WHERE name = ?` Statement.
> Vergiss nicht `conn.commit()` am Ende – sonst wird nichts gespeichert!
> Und beachte die Reihenfolge der Werte: erst der neue Score, dann der Name.

---

## Mini-Übung 2: Spieler löschen

Schreibe eine Funktion `spieler_loeschen(name)`, die einen Spieler komplett aus der Datenbank entfernt.

Gib danach die Highscore-Liste aus, um zu prüfen ob er wirklich weg ist.

> [!tip] Tipp
> ```sql
> DELETE FROM players WHERE name = ?
> ```
> Auch hier gilt: Platzhalter `?` verwenden, nicht den Namen direkt einbauen!
