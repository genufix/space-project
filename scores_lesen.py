import csv

with open("highscores.csv", "r") as datei:
    reader = csv.DictReader(datei)  # Liest die Spaltenbezeichnungen automatisch

    for zeile in reader:
        print(f"{zeile['name']} hat {zeile['score']} Punkte auf Level {zeile['level']} erreicht!")