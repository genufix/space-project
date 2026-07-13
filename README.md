# space-game

**space-game** ist ein Teilprojekt von **[space-project]()** und wurde speziell für die **Praktikantenwoche** vorbereitet.  
Ziel ist es, einen strukturierten Einstieg in die Python- und Spieleentwicklung mit [pygame](https://pyga.me/) zu ermöglichen.  
Das Projekt ist in mehrere Module (Exercises) unterteilt, die jeweils ein abgegrenztes Lernziel verfolgen.

<img src="./assets/docs/showcase.gif" width="50%">

**Jedes Modul enthält:**
* Eine ausführliche **Anleitung** in der jeweiligen `README.md`
* Eine **Musterlösung**, falls man an einer Stelle nicht weiterkommt oder das Ergebnis vergleichen möchte

> [!NOTE] Info:
>
> Du schreibst deinen eigenen Code **nicht** in den `exercises/`-Ordnern, sondern durchgehend in `game/`.  
> Dieser Ordner wächst über alle 11 Module hinweg. Mehr dazu unter [Projektstruktur](#-projektstruktur).

> [!TIP] Tipp:
>
> In jeder Aufgabe erkennst du an **"Führe das Programm jetzt aus"**-Hinweisen, wann ein guter Zeitpunkt ist,  
> das Spiel zu starten und dein Ergebnis zu prüfen. Code-Blöcke ohne weiteren Kommentar kannst du direkt  
> 1:1 übernehmen. Blöcke hinter einem eingeklappten **"Lösung"** sind dagegen als **Aufgabe** gedacht.  
> Versuch dich hier zuerst selbst, bevor du aufklappst.

## 📁 Projektstruktur

```py
space-game/
├── game/                    # Dein Arbeitsordner - hier schreibst du deinen Code
│   ├── main.py              #   Wächst über alle Module hinweg (Modul 1 -> Modul 11)
│   └── settings.py
├── assets/                  # Gemeinsame Assets (Bilder, Sounds, Musik, Fonts)
│   ├── images/
│   ├── sounds/
│   ├── music/
│   ├── fonts/
│   ├── docs/                #   Screenshots/GIFs für die Anleitungen (keine Spiel-Assets)
│   └── ...
├── exercises/               # Kursmaterial: Anleitung + Referenzlösung pro Modul
│   ├── exercise-01/
│   │   ├── README.md        # Anleitung zum Modul
│   │   └── solution/
│   │       └── main.py      # Musterlösung
│   ├── exercise-02/
│   │   └── ...
│   ├── ...
│   └── showcase/            # Kein Modul, nur zum Spielen (siehe unten)
│       └── solution/
├── packages/                  # Fertige, eigenständige Packages (siehe unten)
│   ├── space-game-entities/   # Player-, Projektil- & Asteroiden-Sprites (Aufgabe 5/6)
│   ├── space-game-ui/         # Start-/Pause-/Death-Screen (Aufgabe 10)
│   ├── space-game-utils/      # Debug-Text, HUD, Hintergrund-Kacheln, Geräte-ID & API-Client (Aufgabe 7/8/9)
│   └── space-game-physics/    # pymunk-Wrapper (Aufgabe 11, Bonus)
├── .gitignore
├── pyproject.toml
├── README.md
├── uv.lock
```
(Ausgabe wurde mit [tree](https://manpages.ubuntu.com/manpages/trusty/man1/tree.1.html) erstellt)

## 📚 Module

| Modul | Thema |
| --- | --- |
| [Aufgabe 1](exercises/exercise-01/README.md) | Das erste pygame-Fenster |
| [Aufgabe 2](exercises/exercise-02/README.md) | Inhalt auf der Leinwand anzeigen |
| [Aufgabe 3](exercises/exercise-03/README.md) | Bewegungen mit Tastatureingabe (WASD) |
| [Aufgabe 4](exercises/exercise-04/README.md) | Projektile feuern |
| [Aufgabe 5](exercises/exercise-05/README.md) | Player & Projektile verwenden |
| [Aufgabe 6](exercises/exercise-06/README.md) | Asteroiden verwenden |
| [Aufgabe 7](exercises/exercise-07/README.md) | Kollisionen |
| [Aufgabe 8](exercises/exercise-08/README.md) | Sounds, Musik & Hintergrund |
| [Aufgabe 9](exercises/exercise-09/README.md) | Score an die API senden |
| [Aufgabe 10](exercises/exercise-10/README.md) | Start-, Pause- und Death-Screen |
| [Aufgabe 11](exercises/exercise-11/README.md) | Bonus: Echte Physik mit pymunk (optional) |

> [!TIP] Tipp:
>
> [`exercises/showcase`](exercises/showcase/README.md) ist **kein** weiteres Modul, sondern eine bereits  
> fertig ausgebaute Version zum Spielen (Explosionen, Asteroiden, die sich beim Treffer aufteilen, gegnerische Schiffe).  
> Gut geeignet für die gemeinsame Vorführung am Ende der Praktikumswoche.

## 🗓️ Zeitplan (Empfehlung)

`Player`, `Projectil` und `Asteroid` kommen fertig aus `space-game-entities` (siehe [Fertige Packages](#-fertige-packages)).  
Teilnehmer müssen dafür keine eigenen Klassen schreiben, sondern importieren und verdrahten fertige Bausteine.  

| Tag | Module | Fokus |
| --- | --- | --- |
| 1 | Aufgabe 1-4 | Grundlagen: Fenster, Zeichnen, Bewegung, Projektile |
| 2 | Aufgabe 5-7 | Player & Asteroiden verwenden, Kollisionen |
| 3 | Aufgabe 8-9 | Sounds/Musik/Hintergrund, Score-API |
| 4 | Aufgabe 10 + Puffer/Vorführung | Start-/Pause-/Death-Screen, fertiges Spiel anschauen |

> [!TIP] Tipp:
>
> Am Ende sollte in jedem Fall eine gemeinsame Vorführung des fertigen Spiels stehen (z. B. über die  
> `solution/`-Referenz von Aufgabe 11 oder die ausgebaute Version unter [`exercises/showcase`](exercises/showcase/README.md)),  
> damit alle sehen, worauf das Ganze hinausläuft, auch wenn nicht jeder selbst bis dahin gekommen ist.

## 🧩 Fertige Packages

Manche Themen (ein Menü-System bauen, eine Physik-Engine einbinden) sind für ein Praktikum zu aufwändig,  
um sie komplett selbst zu schreiben. Dafür liegen unter `packages/` fertige, eigenständige Python-Packages,  
die als lokale Abhängigkeiten über einen [uv-Workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/)  
eingebunden sind. Ein `uv sync` reicht, danach lassen sie sich ganz normal importieren:

```python
from space_game_entities import Player, Projectile, Asteroid
from space_game_ui import Menu
from space_game_utils import debug, draw_hud, load_background, get_device_id, ApiClient
from space_game_physics import PhysicsWorld
```

* `space-game-entities`: Fertige `Player`-, `Projectile`- und `Asteroid`-Sprites inkl. Varianten (Aufgabe 5/6);
  `Enemy` & `Explosion` sind zusätzlich enthalten, werden aber nur im [Showcase](exercises/showcase/README.md) genutzt
* `space-game-ui`: Start-, Pause- und Death-Screen inkl. Menü-Musik & Bestätigungs-Sound (Aufgabe 10)
* `space-game-utils`: `debug()`, `draw_hud()`, Hintergrund-Kacheln (`load_background()`),
  Geräte-ID (`get_device_id()`) & API-Client (`ApiClient`) (Aufgabe 7/8/9)
* `space-game-physics`: Vereinfachter pymunk-Wrapper (Aufgabe 11, Bonus)

## Projekt Setup

> [!IMPORTANT] Wichtig:
>
> Führe **beide** Schritte (Klonen **und** `uv sync`) einmal komplett durch, **bevor** du mit
> [Aufgabe 1](exercises/exercise-01/README.md) startest.

### Repository klonen

```sh
git clone git@gitlab.genua.de:azubis/praktikumswochen/space-game.git
```

> [!IMPORTANT] Wichtig:
> 
> Um das Repository zu klonen, muss git auf dem System installiert sein.  
> Den Praktikanten sollte git vorher erklärt werden.

## Umgebung & Abhängigkeiten installieren

### Mit uv: (empfohlen)

```sh
uv sync
```

> [!TIP] Tipp:
>
> `uv sync` installiert nicht nur `pygame-ce`, `httpx` und `pymunk`, sondern auch alle Packages unter
> `packages/` (siehe [Fertige Packages](#-fertige-packages)) als lokale Abhängigkeiten. Ohne diesen Schritt
> schlägt schon der erste `import pygame` in [Aufgabe 1](exercises/exercise-01/README.md) fehl.

Falls `uv` noch nicht installiert wurde:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> [!NOTE] Info:
> 
> Weitere Informationen zur Installation: [uv - Getting Started](https://docs.astral.sh/uv/getting-started/installation/)

### Warum uv?

`uv` ist ein moderner, performanter Paket- und Projektmanager für Python,  
welcher klassische Tools wie `pip`, `venv`, `virtualenv` und `pip-tools` vereint.

### Vorteile:
* **Schnelle** Installation von Python-Versionen & Paketen
  ```sh
  uv python install 3.13 # installiert z.B. Python 3.13.4
  uv [add/remove] <module> # Python Module projektbezogen verwalten
  ```
* **Reproduzierbarkeit** durch Lockfiles (uv.lock)
  ```sh
  uv lock
  uv sync
  ````
* Automatische Verwendung von venv (Virtuelle Umgebung)
  ```sh
  uv run <script_name>.py # fuehrt das Script innerhalb der venv aus
  ```
* Weniger Konflikte und bessere Kompatibilität (z.B. durch Versionsunterschiede)

## Ressourcen

* [pygame-ce (Community Edition)](https://pyga.me/docs/)
* [pymunk (Physik-Engine)](http://www.pymunk.org/en/latest/)
* [httpx](https://www.python-httpx.org/)
* [uv](https://docs.astral.sh/uv/)
