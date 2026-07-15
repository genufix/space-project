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


import sys
import os
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


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))



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

 
