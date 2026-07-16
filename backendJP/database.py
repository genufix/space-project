import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "space_invaders.db")


def get_db():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                device_id   TEXT,
                score       INTEGER DEFAULT 0,
                level       INTEGER,
                datum       TEXT
            )
        """)

        conn.commit()
        print("Datenbank und Tabelle erfolgreich initialisiert!")


init_db()

#def calculate_score(asteroids_destroyed: int, time_lived: float) -> int:
#    if (asteroids_destroyed < 0 or time_lived < 0):
#        raise ValueError ("Keine negativen Werte")
#    return asteroids_destroyed * 100 + int(time_lived)    

#@app.get