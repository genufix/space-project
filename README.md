# space-backend

**space-backend** ist ein Teilprojekt von **[space-project]()** und wurde speziell für die **Praktikantenwoche** vorbereitet.  
Ziel ist es, einen strukturierten Einstieg in die Backend-Entwicklung mit FastAPI und Datenbanken zu ermöglichen.  
Das Projekt bietet eine vollständige REST-API sowie WebSocket-Funktionalität für Live-Score-Updates.

## Übersicht
Dieses Projekt stellt eine moderne Python-Backend-API bereit, die Spiel-Scores speichert und verwaltet. Es nutzt FastAPI für die REST-API, SQLite für die Datenpersistierung und WebSockets für Live-Updates. Das Backend ist containerisiert und kann einfach mit Docker gestartet werden.

## Funktionen
- **REST-API** für Score-Management (POST/GET)
- **SQLite-Datenbank** für persistente Datenspeicherung
- **Automatische Score-Berechnung** basierend auf Asteroiden und Überlebenszeit


## API-Endpunkte

### REST-API
- `POST /score` - Neuen Score einreichen
- `GET /scores` - Top-Scores abrufen
- `GET /docs` - Interaktive API-Dokumentation (Swagger)


## Dateistruktur
- `main.py` – Hauptanwendung mit FastAPI, Datenbankmodellen und Endpunkten
- `pyproject.toml` – Projekt-Konfiguration für uv
- `.gitignore` – Git-Ignore-Regeln


### Hinweise
- Das Backend ist für die Integration mit dem space-frontend und space-game optimiert
