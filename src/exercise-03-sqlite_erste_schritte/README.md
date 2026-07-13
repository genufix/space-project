# Übung 03: SQLite installieren + SQL-Befehle lernen

> [!note] Lernziel:
> Echte Datenbanken. CSV war ein guter Start, aber jetzt steigen wir auf eine richtige Datenbank um. SQLite ist dabei perfekt für den Einstieg.

---

## 1. Was ist SQLite?

SQLite ist ein kostenloses Datenbankprogramm. Der große Unterschied zu anderen Datenbanken: SQLite speichert alles in einer einzigen Datei auf deinem Computer.

**Warum SQLite?**
- Kostenlos und Open Source
- Läuft auf Windows, Mac und Linux
- Perfekt für kleine Projekte und zum Lernen

Mehr Informationen gibt es in der [Dokumentation - SQLite3](https://www.sqlite.org/docs.html).

---

## 2. Installation auf Linux

Öffne ein Terminal und tippe:

```bash
sudo apt update
sudo apt install sqlite3
```

Überprüfe die Installation:
```bash
sqlite3 --version
```

Du solltest etwas wie `3.39.0 2022-07-21` sehen.

---

## 3. Erstelle eine Datenbank

> [!tip] Im Terminal
Für `uv run database.py` aus. Dies ist vor allem für später wichtig.

> [!note] Was ist '.db'?
> Die Dateiendung `.db` steht für „database". SQLite speichert die gesamte Datenbank in dieser einen Datei. Du kannst sie wie eine normale Datei kopieren, verschieben oder löschen.

---

## 4. Die wichtigsten SQL-Befehle

SQL (**S**tructured **Q**uery **L**anguage) ist die Sprache, mit der wir mit Datenbanken kommunizieren. Jetzt lernst du die 5 wichtigsten Befehle – zusammen werden sie **CRUD** genannt.

### 4.1 Tabelle erstellen – `CREATE TABLE`

```sql
CREATE TABLE players (
    CREATE TABLE IF NOT EXISTS players (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        device_id   TEXT,
        score       INTEGER DEFAULT 0,
        level       INTEGER,
        datum       TEXT
);
```

Was bedeutet was?
- `INTEGER` → Eine ganze Zahl (z. B. 42000)
- `TEXT` → Ein Text (z. B. "AstroAlex")
- `PRIMARY KEY` → Diese Spalte ist die eindeutige ID
- `AUTOINCREMENT` → SQLite vergibt die ID automatisch (1, 2, 3, ...)
- `IF NOT EXISTS` → Es wird nur die Tabelle erstellt, wenn sie nicht bereits existiert
- `NOT NULL` → Dieser Wert darf nicht leer gelassen werden

### 4.2 Daten einfügen – `INSERT INTO`

```sql
INSERT INTO  (name, score, level, datum)
VALUES ("AstroAlex", 42000, 5, "2024-06-10");
```

Füge noch zwei weitere Einträge hinzu:
```sql
INSERT INTO players (name, score, level, datum)
VALUES ("GalaxyGreta", 38500, 3, "2024-06-10");

INSERT INTO players (name, score, level, datum)
VALUES ("NebulaNiko", 51200, 7, "2024-06-11");
```

### 4.3 Daten lesen – `SELECT`

Alle Einträge ausgeben:
```sql
SELECT * FROM players;
```

Nur bestimmte Spalten:
```sql
SELECT name, score FROM players;
```

Sortiert nach Score (höchster zuerst):
```sql
SELECT * FROM players ORDER BY score DESC;
```

Nur die Top 3:
```sql
SELECT * FROM players ORDER BY score DESC LIMIT 3;
```

> [!note] Was bedeutet ' * ' ?
> Der Stern steht für „alle Spalten". `SELECT * FROM players` heißt also: „Gib mir alles aus der Tabelle players."
`DESC` steht für „descending" (absteigend), `ASC` für „ascending" (aufsteigend).

### 4.4 Daten ändern – `UPDATE`

```sql
UPDATE players
SET score = 55000
WHERE name = "AstroAlex";
```

> [!Warning] Achtung:
> Vergiss das `WHERE` nicht! Das `WHERE` kannst du dir wie eine `if-Abfrage` aus Python vorstellen. Es gibt an, welche Bedingung erfüllt sein muss, damit an der gewollten Stelle der Eintrag angepasst wird. In Gedanken würdest du **"Aktualisiere den `score` aus der Tabelle `players` auf `55000` wo der `name = 'AstroAlex'` entspricht"** sagen. Ohne `WHERE` würdest du **jeden** `score` von jedem Spieler aus der Tabelle `players` auf `55000` setzen.  

### 4.5 Daten löschen – `DELETE`

```sql
DELETE FROM players
WHERE id = 2;
```

**Auch hier:** Immer `WHERE` angeben, sonst löschst du die gesamten Tabelle-Inhalt!

---

### 4.5 Tabelle löschen – `DROP`

```sql
DROP TABLE players;
```

> [!Warning] Achtung:
> Diesen Befehl kann man (i.d.R) nicht rückgängig machen. 
---

## Mini-Übungen: Werde zum Datenbank-Admin

Führe diese Aufgaben nacheinander in SQLite durch. Lass nach jeder Aufgabe alle Scores mit `SELECT * FROM players;` anzeigen, um das Ergebnis zu kontrollieren.

**Übung 1:** Füge einen neuen Spieler hinzu:
- Name: `"CometCarla"`
- Score: `33000`
- Level: `4`
- Datum: `"2024-06-12"`

**Übung 2:** CometCarla hat eine zweite Runde gespielt und dabei exakt 10.000 Punkte mehr als ihren vorherigen Score erreicht. Aktualisiere ihren Score entsprechend!

**Übung 3:** Lass dir die komplette Rangliste ausgeben – nach Score sortiert, höchster zuerst.

**Übung 4:** NebulaNiko hat gemogelt und soll aus der Rangliste fliegen. Lösche seinen Eintrag.

> [!tip] Tipp für Aufgabe 2 – Rechnen in SQL
> Du musst nicht erst den alten Wert ablesen und dann neu eingeben. Du kannst in SQL direkt rechnen:
> ```sql
> SET score = score + 10000
> ```

> [!tip] Tipp für Aufgabe 4
> Verwende `WHERE name = "NebulaNiko"` oder schau in der Rangliste nach, welche `id` NebulaNiko hat.

---

## 5. Nützliche SQLite-Befehle im Terminal

Diese Befehle funktionieren direkt im SQLite-Prompt (mit Punkt am Anfang – das sind keine SQL-Befehle):

```
.tables          → Zeigt alle Tabellen in der Datenbank
.schema          → Zeigt die Struktur aller Tabellen
.mode column     → Schönere Ausgabe in Spalten
.headers on      → Zeigt die Spaltenbezeichnungen
.quit            → SQLite verlassen
```

---

## 6. Wie geht es weiter?

Du kannst jetzt SQL-Befehle direkt im Terminal eingeben. In **Übung 04** verbindest du Python mit SQLite – damit kannst du diese Befehle automatisch aus einem Programm heraus ausführen. Kein manuelles Tippen mehr!
