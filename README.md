# space-frontend
**space-frontend** ist ein Teilprojekt von **[space-project]()** und wurde speziell für die **Praktikantenwoche** vorbereitet.  
Ziel ist es, eine einfache und anpassbare Web-Oberfläche zur Anzeige eines Spiel-Scoreboards mit HTML, CSS und Javascript zu erstellen
und das Frontend mit einem Backend sowie dem Pygame zu verbinden.
Das Projekt ist in mehrere Module (Exercises) unterteilt, die jeweils einen Teilschritt auf dem Weg zum fertigen Projekt darstellen.

## Übersicht
Dieses Projekt bietet eine statische Web-Oberfläche zur Visualisierung von Benutzerstatistiken und Punktzahlen für ein Spiel. Es ist darauf ausgelegt, leichtgewichtig, einfach zu konfigurieren 
und für die Integration mit jeder Backend-API geeignet zu sein, die Benutzerstatistiken bereitstellt. Konkret bedeutet dass: Das Pygame schickt die Spielerdaten (welcher Spieler wieviele
Punkte erreicht hat) an das Backend. Das Backend verwaltet die Daten in einer Datenbank und macht sie abrufbar. Nun kommen wir ins Spiel. Unser Frontend kann die Daten vom Backend abfragen
und auf einer Homepage anzeigen. Dabei soll das alles noch gut aussehen.

## Funktionen
- Zeigt ein Live-Scoreboard mit Benutzerstatistiken an
- Ruft Daten von einem konfigurierbaren API-Endpunkt ab
- Responsive und saubere Benutzeroberfläche
- Einfach einzurichten und anzupassen

## Verwendung
1. Öffne `scoreboard.html` im Browser.
2. Das Scoreboard wird automatisch Benutzerstatistiken vom konfigurierten API-Endpunkt abrufen und anzeigen.

## Konfiguration
- Die API-Endpunkt-URL kann in der `scoreboard.js`-Datei eingestellt werden.

## Dateistruktur
- `scoreboard.html` – Haupt-HTML-Datei für die Scoreboard-Benutzeroberfläche
- `scoreboard.js` – Behandelt das Abrufen und Anzeigen von Benutzerstatistiken
- `style.css` – Styles für die Scoreboard-Benutzeroberfläche

## Wichtig
In diesem Projekt lernst du viele Techniken kennen und bekommst eine Menge Informationen. Das wichtigste ist es aber **nicht** jeden Teilschritt möglichst schnell zu beenden oder perfekt 
zu machen. Es geht darum das Grundprinzip zu verstehen, wie man ein Web-Frontend aufbauen kann. Die Lösungsvorschläge dienen nur der Orientierung.
Versuche auch immer die Lösung zu verstehen. Warum wird das so gemacht? Würde ich das anders machen? Hab Spaß und probiere immer selbst aus.


Weiter geht es mit der excercise-01 im Ordner src!
