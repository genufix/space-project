# space-game

**space-game** ist ein Teilprojekt von **[space-project]()** und wurde speziell für die **Praktikantenwoche** vorbereitet.  
Ziel ist es, einen strukturierten Einstieg in die Python- und Spieleentwicklung mit pygame zu ermöglichen.  
Das Projekt ist in mehrere Module (Exercises) unterteilt, die jeweils ein abgegrenztes Lernziel verfolgen.

**Jedes Modul enthält:**
* Eine ausführliche **Anleitung** in der jeweiligen `README.md`
* Eine **Musterlösung**, um bei Bedarf eine funktionierende Ausgangsbasis für nachfolgende Module zu gewährleisten

## 📁 Projektstruktur

```py
space-game/
├── src/
│   ├── assets/        # Gemeinsame Assets (Bilder, Sounds, etc.)
│   │   ├── images/
│   │   ├── sounds/
│   │   └── ...
│   ├── exercise_01/
│   │   ├── README.md  # Anleitung zum Modul
│   │   └── main.py    # Musterlösung
│   ├── exercise_02/
│   │   └── ...
│   └── ...
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
```

* `src/exercise_*`: Alle Übungen befinden sich im `src`-Verzeichnis und sind modular aufgebaut
* `src/assets/`: Assets wie Bilder und Sounds, welche von den Übungen verwenden werden, befinden sich in einem zentralen Verzeichnis

## Projekt Setup

### Repository klonen

```sh
git clone git@gitlab.genua.de:azubis/praktikumswochen/space-game.git
```

> [!note]INFO
> 
> Um das Repository zu klonen, muss git auf dem System installiert sein.  
> Den Praktikanten sollte git vorher erklärt werden.

## Umgebung & Abhängigkeiten installieren

### Mit uv: (empfohlen)

```sh
uv venv
uv sync
```

Falls `uv` noch nicht installiert wurde:
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> [!note]INFO
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

### Alternativ: Mit pip

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Ressourcen

* [pygame-ce (Community Edition)](https://pyga.me/docs/)
* [pymunk (Physik-Engine)](http://www.pymunk.org/en/latest/)
* [uv](https://docs.astral.sh/uv/)