import csv 
from datetime import date

with open("highscores.csv","a",newline="") as datei:
    writer=csv.writer(datei)
    writer.writerow(["RocketRobin",29000,2,date.today()])