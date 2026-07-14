import csv
highscore = 0 
bester_spieler = None

with open("highscores.csv", "r")as datei:
    reader = csv.DictReader(datei)
    
    for zeile in reader:
        score=int(zeile["score"])
        if score > highscore:
            highscore = score
            bester_spieler = zeile["name"]
        




