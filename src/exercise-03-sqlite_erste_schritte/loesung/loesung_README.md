### Musterlösung – Mini-Übung 1

```sql
INSERT INTO players (name, device_id, score, level, datum)
VALUES ("CometCarla","63da4cdb-903b-44e4-9ee7-82277496032e", 33000, 4, "2024-06-12");
```

### Musterlösung – Mini-Übung 2

```sql
UPDATE players
SET score = score + 10000
WHERE players = "CometCarla";
```

### Musterlösung – Mini-Übung 3

```sql
SELECT * FROM players ORDER BY score DESC;
```

### Musterlösung – Mini-Übung 4

```sql
DELETE FROM players WHERE name = "NebulaNiko";
-- oder mit der ID (falls z. B. id = 3):
DELETE FROM players WHERE id = 3;
```