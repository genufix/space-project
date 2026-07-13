### Musterlösung – Mini-Übung 1
Schau in POST /spieler – dort steht:
```python
score = 0
```
`calculate_score()` wird dort gar nicht aufgerufen, nur in `PUT /spieler/{id}/scores`.

Der Grund für die Aufteilung:
> - Bei der Registrierung hat der Spieler noch gar keine Runde gespielt – es gibt also noch keine asteroids_destroyed oder time_lived. Der POST-Endpoint legt nur den Spieler an (sozusagen „Konto eröffnen"), der PUT-Endpoint aktualisiert den Score nach einer gespielten Runde.
> - Wenn POST bereits Spieldaten entgegennehmen würde, müsste das Spiel beim ersten Start sofort eine vollständige Runde liefern – das ergibt logisch keinen Sinn. Registrierung und Spielergebnis sind zwei verschiedene Aktionen.


### Musterlösung – Mini-Übung 2
Mit AND müssen beide Bedingungen gleichzeitig zutreffen. Das bedeutet:

> - „AstroAlex" mit einer anderen device_id → Check schlägt nicht an → zweiter Eintrag wird angelegt 
> - Dieselbe device_id mit einem anderen Namen → Check schlägt nicht an → zweiter Eintrag wird angelegt 

Der Check schützt also nur gegen den Fall, dass exakt derselbe Name und dieselbe ID gleichzeitig auftauchen – was in der Praxis kaum passiert. Mit OR wäre es strenger:
```SQL
WHERE name = ? OR device_id = ?
```
Dann würde beides einzeln geblockt – entweder Name oder ID reicht schon aus. OR wäre hier die korrektere Wahl, weil beide Felder eigentlich eindeutig sein sollen.


### Musterlösung – Mini-Übung 3
In diesem Backend nutzen **beide** Endpoints (POST /spieler und PUT /spieler/{id}/scores) Query Parameter. Sauberer wäre es, die Nutzerdaten von POST /spieler als Request Body (JSON) zu übertragen – warum, zeigt der Vergleich:

Query Parameter landen direkt in der URL:
```
PUT /spieler/3/scores?asteroids_destroyed=100&time_lived=180.2
```
Das hat konkrete Nachteile:

> - Server-Logs schreiben die komplette URL mit – alle Werte sind im Klartext in der Logdatei
> - Browser-Verlauf und Proxy-Server speichern URLs – bei sensiblen Daten wie Passwörtern oder Tokens wäre das ein ernstes Sicherheitsproblem
> - URL-Längenlimit – Browser und Server akzeptieren i. d. R. nur URLs bis ca. 2000 Zeichen, bei größeren Datenmengen bricht das ab
> - Ein Request Body (JSON) taucht nicht in der URL auf, hat kein Längenlimit und ist das semantisch korrekte Mittel für POST/PUT-Requests. Query Parameter sind sinnvoll für einfache Filter wie ?limit=10 – nicht für Nutzerdaten.