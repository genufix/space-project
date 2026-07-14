import csv

scores = [
    ["AstroAlex", 42000, 5, "2024-06-10"],
    ["GalaxyGreta", 38500, 3, "2024-06-10"],
    ["NebulaNiko", 51200, 7, "2024-06-11"],
]

with open("highscores.csv", "w", newline="") as datei:
    writer = csv.writer(datei)

    writer.writerow(["name", "score", "level", "datum"])

    writer.writerows(scores)

print("Fertig")