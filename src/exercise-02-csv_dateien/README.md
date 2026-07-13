# Übung 02: In CSV-Datei schreiben

> [!note] Lernziel:
> In dieser Übung speicherst du zum ersten Mal Space Invaders Scores dauerhaft – in einer einfachen CSV-Datei. Und du schreibst dein erstes Python-Skript.

---

## 1. Was ist eine CSV-Datei?

CSV steht für **C**omma-**S**eparated **V**alues – also „durch Komma getrennte Werte".

Eine CSV-Datei ist eine ganz normale Textdatei, die so aussieht:

```
name,score,level,datum
AstroAlex,42000,5,2024-06-10
GalaxyGreta,38500,3,2024-06-10
NebulaNiko,51200,7,2024-06-11
```

Die erste Zeile sind die **Spaltenbezeichnungen** (Header).
Jede weitere Zeile ist ein **Datensatz**.

Du kannst eine CSV-Datei mit jedem Texteditor öffnen – und auch mit Excel oder LibreOffice Calc.

> [!note] Warum CSV?
> CSV-Dateien können von fast jedem Programm gelesen werden. Sie sind einfach zu verstehen und ein perfekter erster Schritt. Danach steigen wir auf richtige Datenbanken um – dann siehst du auch, wo CSV an seine Grenzen stößt.

Mehr Informationen gibt in der [Dokumentation - CSV](https://docs.python.org/3/library/csv.html).

---

## 2. Python-Basics – was du wissen musst

Falls du noch nie Python gesehen hast: kein Problem! Hier sind die wichtigsten Grundlagen für diese Übung.

**Variablen speichern Werte:**
```python
name = "AstroAlex"
score = 42000
```

**Listen speichern mehrere Werte:**
```python
meine_liste = ["Alex", "Greta", "Niko"]
```

**`print()` zeigt etwas im Terminal an:**
```python
print("Hallo Space Invader!")
print(score)  # Gibt 42000 aus
```

**Kommentare beginnen mit `#` – Python ignoriert sie:**
```python
# Das ist ein Kommentar – Python liest das nicht
score = 42000  # Das ist der Highscore
```

**f-Strings – Text und Variablen kombinieren:**
```python
name = "AstroAlex"
print(f"Spieler {name} hat gewonnen!")  # Gibt aus: Spieler AstroAlex hat gewonnen!
```

---

## 3. Eine CSV-Datei schreiben

Python hat ein eingebautes Modul namens `csv`, das uns das Leben leichter macht. Module sind fertige Werkzeugkästen – mit `import` holen wir sie herein.

Erstelle eine neue Datei namens `scores_schreiben.py` und tippe folgendes:

```python
import csv  # Wir laden das csv-Modul

# Die Daten, die wir speichern wollen
scores = [
    ["AstroAlex", 42000, 5, "2024-06-10"],
    ["GalaxyGreta", 38500, 3, "2024-06-10"],
    ["NebulaNiko", 51200, 7, "2024-06-11"],
]

# Datei öffnen und schreiben
with open("highscores.csv", "w", newline="") as datei:
    writer = csv.writer(datei)

    # Erst die Kopfzeile schreiben
    writer.writerow(["name", "score", "level", "datum"])

    # Dann alle Datensätze
    writer.writerows(scores)

print("Fertig! Die Datei wurde gespeichert.")
```

Führe das Skript im Terminal aus:
```bash
uv run scores_schreiben.py
```

Schau danach in den Ordner – es sollte eine Datei `highscores.csv` erschienen sein!

> [!tip] Was bedeutet 'with open(...) as datei'?
> Das ist eine sichere Art, Dateien zu öffnen. Python schließt die Datei automatisch am Ende des `with`-Blocks, egal ob etwas schiefläuft oder nicht. Immer besser als manuell `datei.close()` aufzurufen – das vergisst man leicht.

---

## 4. Eine CSV-Datei lesen

Jetzt lesen wir die gespeicherten Daten wieder aus. Erstelle `scores_lesen.py`:

```python
import csv

with open("highscores.csv", "r") as datei:
    reader = csv.DictReader(datei)  # Liest die Spaltenbezeichnungen automatisch

    for zeile in reader:
        print(f"{zeile['name']} hat {zeile['score']} Punkte auf Level {zeile['level']} erreicht!")
```

```bash
uv run scores_lesen.py
```

**Ausgabe:**
```
AstroAlex hat 42000 Punkte auf Level 5 erreicht!
GalaxyGreta hat 38500 Punkte auf Level 3 erreicht!
NebulaNiko hat 51200 Punkte auf Level 7 erreicht!
```

> [!note] Was ist 'DictReader'?
> Normaler `reader` gibt dir Zeilen als Listen zurück: `["AstroAlex", "42000", "5", ...]`
> `DictReader` gibt dir Zeilen als Wörterbuch zurück: `{"name": "AstroAlex", "score": "42000", ...}`
> Mit dem Wörterbuch kannst du die Spalten beim Namen nennen – das macht den Code viel lesbarer.

---

## Mini-Übung 1: Einen neuen Score hinzufügen

Schreibe ein Skript `neuer_score.py`, das einen neuen Spieler zur Datei **hinzufügt** – ohne die alten Einträge zu löschen!

Füge diesen Spieler hinzu:
- Name: `"RocketRobin"`
- Score: `29000`
- Level: `2`
- Datum: Das heutige Datum

> [!tip] Tipp 1
> Wenn du eine Datei mit `"w"` öffnest, wird sie überschrieben (w = write).
> Um etwas **anzuhängen**, nutze `"a"` (a = append):
> ```python
> with open("highscores.csv", "a", newline="") as datei:
> ```

> [!tip] Tipp 2 – Heutiges Datum
> Das heutige Datum bekommst du so:
> ```python
> from datetime import date
> heute = date.today()
> print(heute)  # z. B. 2024-06-10
> ```

---

## Mini-Übung 2: Den Highscore finden

Schreibe ein Skript `highscore.py`, das alle Scores aus der CSV-Datei liest und den **höchsten Score** samt Spielernamen ausgibt.

**Gewünschte Ausgabe:**
```
Der Highscore gehört NebulaNiko mit 51200 Punkten!
```

> [!tip] Tipp – Zahlen aus CSV
> Werte aus CSV-Dateien werden immer als **Text (String)** eingelesen – auch Zahlen!
> Damit du vergleichen kannst, musst du den Score erst in eine Zahl umwandeln:
> ```python
> score_als_zahl = int(zeile["score"])
> ```

---

## 5. Warum reicht CSV nicht für immer?

CSV-Dateien sind toll für den Anfang, aber sie haben Grenzen:

- Mehrere Programme können nicht gleichzeitig in dieselbe Datei schreiben
- Suchen, Filtern und Sortieren musst du selbst programmieren
- Für viele Datensätze wird es langsam
- Man kann keine Beziehungen zwischen Tabellen abbilden

Genau deshalb gibt es **richtige Datenbanken** siehe übung 03.
