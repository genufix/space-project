# Übung 07 – Daten von einer echten API laden und Fehlerbehandlung

In dieser Übung lernst du Schritt für Schritt, wie du mit `fetch` Daten von einer echten API lädst, Fehler abfängst und dem Nutzer Fehlermeldungen anzeigst. Du verstehst, wie HTTP-Statuscodes, Netzwerkfehler und die DOM-Fehleranzeige zusammenhängen. 
---

## Schritt 1 – Was ist fetch und wie funktioniert es?

Mit `fetch` kannst du Daten von einer URL (z.B. einer API) laden. Das Ergebnis ist ein sogenanntes Promise, also ein Verprechen. Klingt komisch, bedeutet aber bei JS dass eine Aufgabe im Hintergrund ausgeführt wird (asynchron) und das Ergebnis wird
nachgeliefert sobald es da ist. Vorteil: Der restliche Programmcode kann in der Zwischenzeit weiterlaufen und muss nicht warten. Stell dir unser Projekt vor. Wenn unsere Seite beim laden fetch() auf das Backend ausführt, also die Daten vom Backend
abfragen möchte. Das Backend ist aber nicht zu erreichen. Dann würde unsere gesamte Webseite nicht laden, weil der Programmcode an dieser Stelle "stecken" bleibt. Mit Promises und asynchronem Code passiert genau das nicht.


Wir nutzen fetch um die Spielstände vom Backend abzufragen. fetch funktioniert ganz einfach:


Beispiel:
```js
async function getScoreData () {
	try {
		let response = await fetch('https://api.example.com/scoreboard');
		let data = response.text();
		let parsedData = await JSON.parse(data);
	} catch (error) {
		do something in case of error
	}
}

```

- `async function` besagt dass es sich um eine asynchrone Funktion handeln wird.
- `fetch` startet die Anfrage und sagt zur Zieladresse: Gib mir deine Daten! Wir bekommen ein Datenobjekt zurück.
- `https://api.example.com/scoreboard` ist in unserem Beispiel die Zieladresse. Hier müssen wir die Adresse unseres Backend-Servers nehmen.
- `response.text()` gibt uns nur die Daten aus unserem Datenobjekt als ein sogenannter JSON String.
- JSON (JavsScript Object Notation) wird gerne benutzt um Daten im Internet zu verschicken.
- `JSON.parse(data)` wandelt die Antwort von einem JSON-String in ein JavaScript-Objekt um. Das ist besser lesbar für uns.
- `await` sorgt in asynchronen Funktionen dafür, dass wir warten, dass ein Promise erfüllt ist bevor es weitergeht.
- `try` ist der Codeblock, der standardmäßig ausgeführt werden soll.
- `catch` fängt Fehler aus dem try-Block ab, z.B. wenn die API nicht erreichbar ist.

### Aufgabe 1:
- Schreibe ein kleines fetch-Beispiel, das Daten von einer öffentlichen Test-API lädt (z.B. https://jsonplaceholder.typicode.com/todos/1).
- Gib die Antwort mit `console.log` aus.

---

## Schritt 2 – Fehlerarten bei fetch

Es gibt verschiedene Fehler, die beim Laden von Daten auftreten können:
- **Netzwerkfehler:** Die API ist nicht erreichbar (z.B. offline, falsche URL).
- **HTTP-Fehler:** Die API antwortet, aber mit einem Fehlerstatus (z.B. 404, 500).
- **Datenfehler:** Die Antwort ist kein gültiges JSON oder hat das falsche Format.


Du kannst die Fehler untersuchen wenn du im Chrome-Browser oder Firefox einen Rechtsklick machst und auf "Untersuchen" gehst. Dort den Reiter "Netzwerk" auswählen und die Seite neu laden.

### Aufgabe 2:
- Probiere fetch mit einer ungültigen URL aus (z.B. https://irgendwas.gibtsnicht/api) und beobachte, was passiert.
- Probiere fetch mit einer gültigen URL, aber einer Ressource, die nicht existiert (z.B. https://jsonplaceholder.typicode.com/404).
- Beobachte, wie sich die Fehler unterscheiden.

---

## Schritt 3 – HTML-Struktur für Fehlermeldungen

Im Projekt gibt es ein eigenes Element für Fehlermeldungen:
```html
<div id="error-message" class="hidden"></div>
```
- Dieses Element wird per JavaScript sichtbar gemacht, wenn ein Fehler auftritt.

### Aufgabe 3:
- Baue das Element `<div id="error-message" class="hidden"></div>` in deine Seite ein.
- Schreibe mit JavaScript einen Text in das Element und blende es ein. Überlege: Was musst du ändern um das Element sichtbar zu machen?
- **Experimentiere:** Ändere die CSS-Klasse und beobachte, wie sich die Anzeige verändert.

---

## Schritt 4 – CSS für Fehlermeldungen

Wir möchten unsere Fehlermeldungen auffällig gestalten:
```css
#error-message {
    color: #b00020;
    margin-top: 1rem;
    font-size: 1rem;
}
.hidden {
    display: none;
}
```
- Die Klasse `.hidden` blendet das Element aus.

### Aufgabe 4:
- Übernehme die CSS-Styles und passe sie nach Wunsch an (z.B. Hintergrundfarbe, Rahmen).
- **Programmieraufgabe:** Schreibe eine eigene CSS-Klasse, die Fehlermeldungen animiert einblendet (z.B. mit `@keyframes`).

---

## Schritt 5 – Die Funktion showError

Im Projekt soll es eine Funktion geben, die eine Fehlermeldung im DOM anzeigt:
Die Funktion setzt den Text und entfernt die Klasse `hidden`.

### Aufgabe 5:
- Schreibe die Funktion `showError` selbst.
- Rufe sie mit einem eigenen Text auf und beobachte, was passiert.
- **Programmieraufgabe:** Baue ein, dass die Fehlermeldung nach 3 Sekunden wieder verschwindet (Tipp: `setTimeout`).

---

## Schritt 6 – fetch mit Fehlerbehandlung

Die Score-Daten werden per fetch geladen:

```js
async function updateScore() {                                                                   
        try {                                                                                    
                let response = await fetch(apiURL);                                                   
                let data = await response.text();
                let scores = await JSON.parse(data);

		renderScoreboard(scores);
                                                                                                 
        } catch (err) {                                                                          
                showError('Fehler beim Laden der Daten: ' + err.message);                        
        }                                                                                        
};                                                                                               

```
- Die Funktion `showError` soll nun Fehler beim Laden oder Anzeigen der Daten melden.

### Aufgabe 6:
- Nun möchten wir, dass die Abfrage nicht nur einmal, sondern immer wieder automatisch passiert. Wie könntest du das lösen?
- Tipp: recherchiere zur setInterval() Funktion

### Aufgabe 7:
- Mache die folgenden Aufgaben in einem extra Ordner. Dort kannst du das alles aus der HTML und CSS Datei, 
  sowie aus scoreboard.js kopieren.
- Schreibe selbst eine fetch-Logik, die Daten von einer (Test-)API lädt und Fehler behandelt.
- Simuliere einen Fehler (z.B. falsche URL) und beobachte, was passiert.
- **Programmieraufgabe:** Baue einen Button ein, mit dem du die fetch-Anfrage manuell auslösen kannst.
- Nur wenn noch genug Zeit: (**Programmieraufgabe:** Zeige eine Ladeanzeige an, solange die Daten geladen werden.)

---

## Schritt 8 – Mini-Experimente & Verständnisfragen
- Was passiert, wenn die API sehr langsam antwortet?
- Wie würdest du verhindern, dass mehrere Fehlermeldungen gleichzeitig angezeigt werden?
- Wie kannst du die Fehlermeldung automatisch ausblenden, wenn der Nutzer eine Aktion ausführt?
- **Programmieraufgabe:** Schreibe eine Funktion, die die Fehlermeldung mit einer Animation ausblendet.
- **Programmieraufgabe:** Baue einen Button ein, der die Fehlermeldung wieder ausblendet.

---

## Herzlichen Glückwunsch
Du solltest nun ein funktionierendes Frontend haben, das die Spielerdaten aus der Datenbank anzeigt. 
Damit hast du die wichtigsten Grundlagen für die Webentwicklung kennen gelernt.
Die folgenden Übungen zeigen dir wie du dein Frontend noch besser machen kannst. 
Schau sie dir gerne an oder experimentiere mit dem bisher gelernten und probiere deine Webseite so zu 
bauen wie es dir gefällt. **Aber Vorsicht** kopiere dir alle Dateien die du bisher erstellt hast oder 
arbeite am besten in einem neuen Ordner "Experimente" damit du nicht aus Versehen etwas kaputt machst.

 
**Viel Spaß!** 
---
