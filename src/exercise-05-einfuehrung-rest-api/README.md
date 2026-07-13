# Übung 05: REST-API Grundlagen

> [!note] Lernziel:
> Du verstehst, was eine API ist, wie REST-APIs aufgebaut sind, und kannst eine echte API im Browser "live" beobachten.

## Die Kellner-Analogie

Stell dir ein Restaurant vor. Du sitzt am Tisch (das ist dein **Programm**, z. B. eine Webseite). In der Küche steht der Koch (das ist die **Datenbank** mit allen Infos). Du gehst aber nicht selbst in die Küche und durchsuchst die Töpfe – das wäre chaotisch und würde sehr lange dauern. Stattdessen sagst du es dem **Kellner**: "Ich möchte bitte X." Der Kellner gibt das in die Küche weiter und bringt dir die Antwort.

Genau dieser Kellner ist eine **API** (Application Programming Interface) – eine feste, verständliche Art, wie zwei Programme miteinander reden, ohne dass das eine Programm wissen muss, wie das andere intern funktioniert.

Eine **REST-API** ist einfach eine API, die sich an ein paar feste Regeln hält – diese Regeln lernst du jetzt.

## Die vier wichtigsten "Bestellungen" (HTTP-Methoden)

Genau wie ein Kellner nur ein paar feste Sätze versteht (bestellen, ändern, stornieren …), kennt eine REST-API vier wichtige Methoden:

| Methode | Bedeutung | Scoreboard-Beispiel |
|---|---|---|
| `GET` | "Zeig mir …" | `GET /spieler` → alle Spieler anzeigen |
| `POST` | "Erstell mir …" | `POST /spieler` → neuen Spieler anlegen |
| `PUT` | "Ändere …" | `PUT /spieler/3` → Spieler Nr. 3 ändern |
| `DELETE` | "Lösch …" | `DELETE /spieler/3` → Spieler Nr. 3 entfernen |

Jede dieser "Bestellungen" geht an eine **URL** – die Adresse, unter der die API erreichbar ist, z. B. `http://meinebackend.de/spieler`.

Mehr Informationen gibt es in der [Dokumentation - Endpoints](https://developer.mozilla.org/de/docs/Web/HTTP/Reference/Methods).

## Antworten und Status-Codes

Nachdem die API etwas erledigt hat, antwortet sie mit einem **Status-Code** – einer kurzen Zahl, die sagt, was passiert ist:

| Code | Bedeutung |
|---|---|
| `200` | Alles ok |
| `201` | Erfolgreich erstellt |
| `404` | Nicht gefunden |
| `500` | Fehler beim Server |

Diese Codes kennst du vielleicht schon, ohne es zu wissen: Die berühmte "404 – Seite nicht gefunden" ist genau so ein Status-Code.

Mehr Informationen gibt es in der [Dokumenation - Statuscodes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status).

## Die Sprache der Antworten: JSON

APIs antworten fast immer im Format **JSON** (JavaScript Object Notation) – einer simplen Schreibweise für Daten mit Schlüssel und Wert:

```json
{
  "id": 3,
  "name": "Mia",
  "punkte": 1300
}
```

Das ist nichts anderes als eine geordnete Liste von Eigenschaften – leicht für Menschen lesbar und leicht für Programme verarbeitbar.

### Mini-Übung: Eine echte API live ansehen
Öffne in deinem Browser folgende Adresse:

```
https://pokeapi.co/api/v2/pokemon/pikachu
```

Das ist eine echte, öffentliche REST-API über Pokémon! Du siehst die rohe JSON-Antwort. Suche darin: Wie viel wiegt Pikachu (`weight`)? Welche Typen hat es (`types`)? Probier danach eine andere Adresse aus, z. B. mit `charizard` statt `pikachu`. Die API kennt leider nur englische Namen.

### Kurzes Quiz
Welche HTTP-Methode würdest du für folgende Aktionen benutzen?

1. Du willst die komplette Bestenliste anzeigen.
2. Du willst einen falsch eingetragenen Spielernamen korrigieren.
3. Du willst einen neuen Highscore eintragen.
4. Du willst einen Spieler endgültig aus der Liste entfernen.

> [!note] Wieso öffnet der Browser nur 'GET'-Anfragen?
> Wenn du eine Adresse in die Adresszeile eingibst, kann dein Browser nur "Zeig mir …" sagen. Für `POST`, `PUT` und `DELETE` braucht man entweder eigenen Code oder spezielle Tools. Genau diesen Code schreiben wir in der nächsten Übung selbst!

## Das hast du heute gelernt
- [ ] Was eine API ist und wofür man sie braucht
- [ ] Die vier wichtigsten HTTP-Methoden: GET, POST, PUT, DELETE
- [ ] Was Status-Codes wie 200 oder 404 bedeuten
- [ ] Wie JSON aufgebaut ist
- [ ] Wie man eine echte API im Browser ansieht

## Was kommt als Nächstes?
Bisher hast du nur APIs angeschaut, die **andere** gebaut haben. Jetzt wird's ernst: In der nächsten Übung baust du deine **eigene** API – mit einem Tool namens FastAPI. Du wirst selbst der Kellner sein!
