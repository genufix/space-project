# Übung 01: Datenbank-Grundlagen

> [!note] Lernziel:
> Du erfährst die Grundlagen zum wichtigsten Thema - Die Datenbank.
---

## 1. Warum brauchen wir überhaupt eine Datenbank?

Stell dir vor: Du spielst Space Invaders und erreichst einen neuen Highscore – 42.000 Punkte!
Aber dann machst du das Fenster zu und auf einmal ist alles weg.

Das Problem: Ein laufendes Programm merkt sich Daten nur im **Arbeitsspeicher (RAM)** – und der wird beim Beenden geleert. Wie ein Whiteboard, das nach jeder Stunde gewischt wird.

**Die Lösung: Eine Datenbank.**
Eine Datenbank speichert Daten **dauerhaft auf der Festplatte** – also auch wenn der Server neustartet oder das Spiel geschlossen wird. Spielstände, Benutzernamen, Highscores – alles bleibt erhalten und kann jederzeit wieder abgerufen werden.

> [!Tip] Fun Fact:
> Fast jede App, die du kennst, nutzt eine Datenbank im Hintergrund. Instagram speichert deine Posts, Spotify deine Playlists, und wir – unsere Space Invaders Scores! Der einzige Unterschied ist die Größe.

---

## 2. Was ist eine Datenbank?

Eine Datenbank ist wie eine sehr organisierte Excel-Tabelle – nur viel mächtiger und schneller.

Sie besteht aus **Tabellen**. Jede Tabelle hat:
- **Spalten** (auch „Felder" genannt) → beschreiben, *was* gespeichert wird
- **Zeilen** (auch „Datensätze" genannt) → ein konkreter Eintrag

Hier ein Beispiel für unsere Space Invaders Highscore-Tabelle:

| id | name  | score | level | datum      |
|----|--------------|-------|-------|------------|
| 1  | AstroAlex    | 42000 | 5     | 2024-06-10 |
| 2  | GalaxyGreta  | 38500 | 3     | 2024-06-10 |
| 3  | NebulaNiko   | 51200 | 7     | 2024-06-11 |

**Was bedeutet was?**
- `id` → Eine eindeutige Nummer für jeden Eintrag
- `name` → Der Name des Spielers
- `score` → Die erreichte Punktzahl
- `level` → Das höchste erreichte Level
- `datum` → Wann wurde gespielt?

> [!note] Warum brauche ich eine 'id'?
> Was, wenn zwei Spieler denselben Namen haben – z. B. zweimal „Max"? Mit einer eindeutigen ID können wir trotzdem jeden Eintrag klar unterscheiden. Das ist wie eine Schüler-ID in der Schule – du bist nicht der einzige „Max", aber deine Nummer ist einmalig.

---

## 3. Wichtige Begriffe auf einen Blick

| Begriff | Bedeutung | Beispiel |
|---------|-----------|---------|
| **Datenbank** | Der gesamte „Behälter" mit allen Daten | `space_invaders.db` |
| **Tabelle** | Eine Liste mit gleichartigen Daten | `highscores` |
| **Spalte / Feld** | Eine Kategorie in der Tabelle | `name`, `score` |
| **Zeile / Datensatz** | Ein einzelner Eintrag | AstroAlex mit 42000 Punkten |
| **Primärschlüssel** | Die eindeutige ID eines Eintrags | `id = 3` |

---

## 4. Verschiedene Arten von Datenbanken

Es gibt nicht nur eine Art von Datenbank. Die zwei häufigsten:

**Relationale Datenbanken (SQL)**
- Daten werden in Tabellen gespeichert
- Tabellen können miteinander verknüpft werden
- Beispiele: SQLite, PostgreSQL, MySQL
- Wir nutzen diese!

**Nicht-relationale Datenbanken (NoSQL)**
- Daten werden anders strukturiert (z. B. als JSON-Dokumente)
- Flexibler für bestimmte Anwendungsfälle
- Beispiele: MongoDB, Firebase
- Für unseren Kurs nicht nötig

---+

## Mini-Übung 1: Tabelle auf Papier entwerfen

Stell dir vor, du baust ein Space Invaders Spiel mit folgenden Anforderungen:

- Spieler sollen sich mit einem Namen anmelden können
- Jeder Spieler kann mehrere Scores haben (von verschiedenen Runden)
- Du möchtest wissen, auf welchem Level der Score erreicht wurde

**Aufgabe:** Zeichne auf einem Blatt Papier (oder im Editor) eine oder mehrere Tabellen.
Überlege: Welche Spalten brauchst du? Welche Daten willst du speichern?

> [!tip] Tipp 1
> Überlege zuerst: Was sind die „Dinge" in deinem System? Spieler? Scores?
> Für jedes „Ding" könnte eine eigene Tabelle sinnvoll sein.


> [!tip] Tipp 2
> Denk an die Verbindung zwischen Spieler und Score: Ein Spieler hat viele Scores.
> Das nennt man eine **1-zu-n-Beziehung**. Du könntest im Score-Eintrag eine `spieler_id` speichern, die auf den Spieler verweist – so weiß man immer, wer welchen Score hat.

---

##  Mini-Übung 2: Fehler finden

Schau dir diese Tabelle an. Was ist daran problematisch?

| name | score | name |
|-------------|-------|-------------|
| Alex        | 1000  | Alex        |
| Alex        | 2000  | Alex        |


> [!tip] Tipp
> Spalten sollten eindeutige Namen haben. Und: Wenn der Spielername zweimal vorkommt, wie unterscheidest du > die beiden Einträge? Was fehlt außerdem?

---

## 5. Wie geht es weiter?

In **Übung 02** speicherst du zum ersten Mal echte Daten – in einer CSV-Datei mit Python. CSV ist eine sehr einfache Variante von einer Datenbank, ein perfekter erster Schritt aber keine langfristige und schöne Lösung. 

Deswegen steigen wir danach Schritt für Schritt tiefer ein, bis wir am Ende ein vollständiges Backend, was auch so täglich genutzt wird, für unser Space Invaders Spiel haben.
