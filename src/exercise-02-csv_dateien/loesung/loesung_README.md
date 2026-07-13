### Musterlösung – Mini-Übung 1

```python
import csv
from datetime import date

with open("highscores.csv", "a", newline="") as datei:
    writer = csv.writer(datei)
    writer.writerow(["RocketRobin", 29000, 2, date.today()])

print("Neuer Eintrag hinzugefügt!")
```

### Musterlösung – Mini-Übung 2

```python
import csv

bester_spieler = None
bester_score = 0

with open("highscores.csv", "r") as datei:
    reader = csv.DictReader(datei)

    for zeile in reader:
        score = int(zeile["score"])
        if score > bester_score:
            bester_score = score
            bester_spieler = zeile["name"]

print(f"Der Highscore gehört {bester_spieler} mit {bester_score} Punkten!")
```