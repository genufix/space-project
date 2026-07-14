CREATE TABLE players (
    CREATE TABLE IF NOT EXISTS players (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        device_id   TEXT,
        score       INTEGER DEFAULT 0,
        level       INTEGER,
        datum       TEXT
);

INSERT INTO (name, score, level, datum)
VALUES ("AstroAlex", 42000, 5, "2024-06-10");

INSERT INTO players (name, score, level, datum)
VALUES ("GalaxyGreta", 38500, 3, "2024-06-10");

INSERT INTO players (name, score, level, datum)
VALUES ("NebulaNiko", 51200, 7, "2024-06-11");