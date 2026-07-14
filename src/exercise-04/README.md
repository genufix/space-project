# Übung 4 – Die Tabelle mit JavaScript dynamisch füllen

In dieser Übung lernst du, wie du mit JavaScript die Elemente einer Website verändern kannst um später die Tabelle dynamisch mit den Spielerdaten zu füllen.

---

## Schritt 1 – Was ist das DOM und wie kann man es mit JavaScript verändern?

Mit HTML haben wir gelernt, das Gerüst und die Bestandteile einer Webseite zu erstellen. Und mit CSS können wir diese Bestandteile optisch verändern, damit sie anders aussehen. Im Grundsatz ist so eine Webseite
aber immer "fest" oder statisch nachdem sie im Browser geladen wurde. Du gibst eine Adresse im Browser ein > es gibt eine Anfrage > es gibt eine Antwort > und die Seite wird so dargestellt. Fertig. Damit sich auf
der Seite nun etwas verändert brauchen wir JavaScript. JavaScript ist sehr gut darin, den Code von HTML Dateien zu verändern und ist darum eine der beliebtesten Sprachen in der Webentwicklung.


Im Kern kann man JS (JavaScript) ähnlich wie CSS verwenden: Wir wählen die Elemente aus mit denen wir arbeiten wollen, und schreiben dann die Aktion die wir ausführen wollen. Ähnlich zu den Selektoren und Attributen
in CSS. Es gibt ein paar Grundbegriffe zu verstehen.


Das **DOM** steht für (Document Object Model) und ist die Struktur, die der Browser aus deinem HTML erzeugt. Aus jeder Seite die der Browser lädt macht er ein DOM. Mit JavaScript kannst du das DOM verändern – zum Beispiel neue Zeilen in eine Tabelle einfügen.


Mit **Funktionen** beschreiben wir was wir tun möchten. Um eine HTML Seite zu verändern muss meistens vorher das Element bestimmt werden, an dem wir etwas ändern möchten. Funktionen werden so geschrieben: Funktionsname(Argumente) {Code der Funktion};


**Datentypen** oder Datenstrukturen sind Möglichkeiten um Daten in JS aufzubewahren, damit wir damit abeiten können. Ein einfacher Datentyp wäre eine Variable, `var` oder `let`. Du kannst der Variablen einen Namen geben und etwas darin speichern.


Ein weiterer Datentyp sind **Arrays**. Arrays sind einfach eine Liste von mehreren Daten hintereinander. Dabei bekommt jeder Eintrag eine feste Nummer, einen sogenannten Index. Dieser startet bei 0. Der erste Eintrag ist also 
ArrayName[0] und der zweite Eintrag ArrayName[1] usw. In der nächsten Einheit wirst du noch mehr über Arrays erfahren.


Variablen leben in der Regel nur solange das Programm läuft. Wenn du die Webseite also schließt sind die Variablen verschwunden. Außer natürlich du speicherst sie irgendwo.

Zum Beispiel:<br>
- Mit `let VariablenName = Inhalt;`kannst du Daten in einer Variablen speichern.
- Mit `document.querySelector()` kannst du ein Element im HTML auswählen.
- Mit den Funktionen `innerHTML` oder `appendChild()` kannst du den Inhalt verändern oder neue Elemente hinzufügen.

### Aufgabe:
- Recherchiere: Was ist der Unterschied zwischen `innerHTML` und `appendChild()`? Schau dich dazu auf den Links um, die du zu den vorherigen Aufgaben bekommen hast (Stichwort JavaScript Reference).
- In unserer HTML Datei: Versuche mit Javascript den Inhalt eines Elements zu verändern. Welche Schritte sind dafür nötig? innerHTML oder innerText könnten dabei nützlich sein.
- Erstelle einen Knopf / Button irgendwo auf deiner Seite. Recherchiere zu EventListeners um eine Funktion an den Knopf zu hängen. Lass zum Beispiel den Inhalte eines Elements anders werden oder lass ein Element verschwinden wenn du den Knopf drückst.
- Tipp: Hierzu Javascript verwenden um CSS Eigenschaften zu verändern (schau mal nach HTML classList und CSS Attribut visibility).

---

## Schritt 2 – Ein Array mit Score-Daten anlegen

Lege in einer neuen Datei `scoreboard.js` ein Array mit Objekten an, z.B.:

```js
const scores = [
    { name: "Alice", score: 1200 },
    { name: "Bob", score: 950 },
    { name: "Charlie", score: 800 }
];
```

### Aufgabe:
- Ergänze das Array um mindestens zwei weitere Spieler mit eigenen Punktzahlen.

---

## Schritt 3 – Schreibe eine Funktion, die die Tabelle füllt

Die Folgende Funktion sieht auf den ersten Blick schon ziemlich kompliziert aus. Aber das täuscht. Versuche zu verstehen was hier passiert.
Schreibe in `scoreboard.js` eine Funktion, die das Array auswählt und die Tabelle füllt:

```js
function renderScoreboard(scores) {
    // Sort scores from highest to lowest and take the top 10
    scores.sort(function(a, b) { return b.score - a.score; });
    var topScores = scores.slice(0, 10);

    // Fill the table body
    var tbody = document.querySelector('#scoreboard tbody');
    tbody.innerHTML = '';
    for (var i = 0; i < topScores.length; i++) {
        var entry = topScores[i];
        var tr = document.createElement('tr');
        tr.innerHTML =
            '<td>' + (i + 1) + '</td>' +
            '<td>' + entry.name + '</td>' +
            '<td>' + entry.score + '</td>';
        tbody.appendChild(tr);
    }
}
```

Rufe die Funktion am Ende der Datei auf:

```js
renderScoreboard(scores);
```

### Aufgabe:
- Schritt 4 muss erledigt sein bevor dein JS funktioniert!
- Sortiere das Array vor dem Anzeigen nach der Punktzahl (höchste zuerst).
- Probiere aus, was passiert, wenn das Array leer ist.

---

## Schritt 4 – Script im HTML einbinden

Füge in deiner `scoreboard.html` vor dem schließenden `</body>`-Tag ein:

```html
<script src="scoreboard.js"></script>
```

Achte darauf, dass der Pfad stimmt und die Datei im gleichen Ordner liegt!

---

## Schritt 5 – Teste deine Seite

Speichere alle Dateien und öffne `scoreboard.html` im Browser. Die Tabelle sollte jetzt mit den Daten aus dem Array gefüllt werden!

---

