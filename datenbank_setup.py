from database import get_db

with get_db() as conn:
    cursor = conn.cursor()

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

    conn.commit()
    print("Datenbank ist bereit.")