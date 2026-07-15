CREATE TABLE players (
    CREATE TABLE IF NOT EXISTS players (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        device_id   TEXT,
        score       INTEGER DEFAULT 0,
        level       INTEGER,
        datum       TEXT
);