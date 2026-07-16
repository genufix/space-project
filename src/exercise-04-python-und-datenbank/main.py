import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from backendJP.database import get_db
# Den obigen Code nicht entfernen

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
    
    
