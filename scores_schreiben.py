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