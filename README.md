# space-project

Willkommen zu den Praktikumswochen! Dieses Repository enthält die drei
Teilprojekte des Space-Invaders-Praktikums. Jedes Projekt liegt in einem
eigenen Branch – dort findest du die Übungen (Aufgabenstand). Die
Musterlösungen liegen gesammelt im `Loesung`-Branch.

## Projekte (Branches)

| Projekt | Branch | Beschreibung |
|---|---|---|
| Frontend | [`space-frontend`](https://github.com/genufix/space-project/tree/space-frontend) | Scoreboard-Webseite (HTML/CSS/JS), 11 Übungen |
| Backend | [`space-backend`](https://github.com/genufix/space-project/tree/space-backend) | REST-API mit FastAPI & SQLite, 7 Übungen |
| Game | [`space-game`](https://github.com/genufix/space-project/tree/space-game) | Space-Invaders-Spiel mit pygame (Startzustand) |
| Lösungen | [`Loesung`](https://github.com/genufix/space-project/tree/Loesung) | Musterlösungen aller drei Projekte (nach Unterordnern getrennt) |

## Repository klonen

```sh
git clone git@github.com:genufix/space-project.git
cd space-project
```

## Ein Projekt auschecken

Wechsle in den Branch des Projekts, an dem du arbeiten möchtest:

```sh
git checkout space-frontend   # oder space-backend / space-game
```

Jeder Projekt-Branch enthält das jeweilige Projekt direkt im Wurzelverzeichnis
inklusive der Übungen unter `src/`. Eine projekteigene `README.md` erklärt die
Einrichtung und die Übungen im Detail.

## Lösungen

Die Musterlösungen liegen im Branch
[`Loesung`](https://github.com/genufix/space-project/tree/Loesung), getrennt
nach Projekt:

```
Loesung/
├── space-frontend/   # Lösung zum Frontend
├── space-backend/    # Lösung zum Backend
└── space-game/       # vollständiges Spiel
```

Auschecken mit:

```sh
git checkout Loesung
```
