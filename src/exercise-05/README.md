# Übung 5 – Scoreboard dynamisch mit JavaScript füllen - Wiederholung und Vertiefung

In dieser Einheit beschäftigst du dich genauer damit, wie Arrays und Objekte funktionieren, wie du mit dem DOM arbeitest und wie du mit JavaScript HTML erzeugst.

---

## Schritt 1 – Was sind Arrays und Objekte in JavaScript?

Ein **Array** ist eine Liste von Werten. Ein **Objekt** ist eine Sammlung von Eigenschaften (key-value-Paaren).

Beispiel:
```js
const scores = [
    { player: "Alice", score: 1200 },
    { player: "Bob", score: 950 }
];
```
Jedes Element im Array "scores" ist ein Objekt mit den Eigenschaften `player` und `score`.

### Aufgabe 1:
- Schreibe selbst ein Array mit mindestens drei eigenen Spielern und Punktzahlen. Recherchiere hierzu bei Bedarf zu Arrays.
- Erkläre in eigenen Worten, was ein Array und was ein Objekt ist.

---

## Schritt 2 – Das DOM und querySelector

Das **DOM** (Document Object Model) ist die Struktur, die der Browser aus deinem HTML erzeugt. Mit `document.querySelector()` kannst du ein Element im HTML auswählen.

Beispiel:
```js
const tbody = document.querySelector('#scoreboard tbody');
```
Das sucht das `<tbody>`-Element in der Tabelle mit der ID `scoreboard`.

### Aufgabe 2:
- Wir wiederholen ein wenig zu CSS:
- Probiere im Browser-Dev-Tool aus, wie du verschiedene Elemente auswählst (z.B. `document.querySelector('h1')`).
- Was passiert, wenn du ein Element auswählst, das es nicht gibt?

---

## Schritt 3 – forEach und dynamisches HTML erzeugen

Die `for-Schleife` haben wir bereits kennen gelernt. Eine weitere Schleife in JS ist die forEach-Schleife. Mit `forEach` kannst du über alle Elemente eines **Arrays** gehen und für jedes Element etwas tun.

Beispiel:
```js
scores.forEach(function(entry, idx) {
    // entry ist das aktuelle Objekt, idx die laufende Nummer
    // Hier kannst du z.B. eine Tabellenzeile erzeugen
});
```

Mit `document.createElement('tr')` erzeugst du eine neue Tabellenzeile. Mit `innerHTML` kannst du den Inhalt setzen.

### Aufgabe 3:
- Schreibe eine Schleife, die für jeden Spieler im Array eine Zeile in der Konsole ausgibt (z.B. "1. Alice: 1200 Punkte").
- Erkläre, was der Unterschied zwischen `forEach` und einer klassischen `for`-Schleife ist.

---

## Schritt 4 – Die renderScoreboard-Funktion

Nun schauen wir uns die renderScoreboard-Funktion noch einmal genauer an. Diese Funktion füllt die Tabelle:

```js
function renderScoreboard(scores) {
    const tbody = document.querySelector('#scoreboard tbody');
    tbody.innerHTML = '';
    scores.forEach(function(entry, idx) {
        const tr = document.createElement('tr');
        tr.innerHTML =
            '<td>' + (idx + 1) + '</td>' +
            '<td>' + entry.name + '</td>' +
            '<td>' + entry.score + '</td>';
        tbody.appendChild(tr);
    });
}
```
**Erklärung:**
- `tbody.innerHTML = ''` leert die Tabelle, damit sie nicht doppelt gefüllt wird.
- Für jeden Spieler wird eine neue Zeile erzeugt und angehängt.

### Aufgabe 4:
- Schreibe die Funktion selbst und erkläre, was jede Zeile macht.
- Was passiert, wenn das Array leer ist?
- Baue einen Test ein: Was passiert, wenn ein Spieler keinen Namen hat?
- Es gibt oft viele Wege zum Ziel. Fällt dir ein wie wir das selbe Ergebnis erreichen können ohne das `document.createElement('tr')`? 

---

## Schritt 5 – Sortieren und Aufrufen

Mit `scores.sort(function(a, b) { return b.score - a.score; });` sortierst du das Array absteigend nach Punkten.

### Aufgabe 5:
- Sortiere das Array vor dem Anzeigen und erkläre, wie die Sortierfunktion funktioniert.
- Rufe die Funktion `renderScoreboard(scores)` selbst auf.
- Probiere aus, was passiert, wenn du das Array leer machst oder einen Spieler mit gleichem Score einfügst.

---

## Schritt 6 – Script im HTML einbinden - Wiederholung

Du hast in deiner `scoreboard.html` vor dem schließenden `</body>`-Tag ein folgendes eingefügt:
```html
<script src="scoreboard.js"></script>
```

### Aufgabe 6:
- Erkläre, warum das Script am Ende des HTMLs eingebunden werden sollte.
- Was passiert, wenn du es im `<head>` einbindest?

---

## Mini-Experimente & Verständnisfragen
- Was passiert, wenn du `tbody.innerHTML = ''` weglässt?
- Wie begrenzen wir die Tabelle auf maximal 10 Einträge? Wie könnten wir die Tabelle noch begrenzen? (Tipp: Schleife)
- Wie würdest du einen neuen Spieler per JavaScript hinzufügen?

---
