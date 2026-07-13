# Übung 2 – CSS: Dein Scoreboard bekommt Stil

In dieser Übung lernst du, wie du mit CSS deiner Seite ein modernes Aussehen gibst. Du legst eine eigene CSS-Datei an, bindest sie korrekt ein und gestaltest die ersten Elemente.

---

## Schritt 1 – Was ist CSS?

CSS steht für **Cascading Style Sheets**. Damit bestimmst du das Aussehen deiner Webseite: Farben, Schriftarten, Abstände, Layout, Animationen und vieles mehr.

CSS besteht aus:
- **Selektoren** (z.B. `body`, `.scoreboard-wrapper`), die angeben, welche Elemente gestaltet werden.
- **Eigenschaften** (z.B. `color`, `background`, `font-family`) legen das Aussehen fest.  


Oder anders gesagt. Wir wählen das Element aus, was wir gestalten möchten (Selektor) und bestimmen dann die Eigenschaften (mach die Textfarbe blau).<br>

### Aufgabe:

- Du solltest schon etwas über die **Rangfolge von Selektoren und Konkurrenzen** gehört haben. 
- Überlege noch einmal wie du ein Element ganz genau für CSS auswählen kannst, mithilfe von Klassen, Element-im-Element und anderen Methoden.
- Recherchiere: Was ist der Unterschied zwischen einem Tag-Selektor (`body`) und einem Klassen-Selektor (`.scoreboard-wrapper`)?<br>
- Quellen:
[mdn docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors) oder [w3schools](https://www.w3schools.com/cssref/index.php)
---

## Schritt 2 – Lege eine CSS-Datei an

Lege im deinem Projektordner eine Datei mit dem Namen `scoreboard.css` an.

---

## Schritt 3 – Binde die CSS-Datei im HTML ein

Öffne deine `.html` und füge im `<head>`-Bereich **diesen Link** ein:

```html
<link rel="stylesheet" href="scoreboard.css">
```

**Achte darauf, dass der Dateiname und der Pfad stimmen!**

### Aufgabe:
- Wiederhole nocheinmal was ein `<link>` tag ist und wie er funktioniert.
- Was passiert, wenn du dich im Dateinamen vertippst? Probiere es aus!
- Recherchiere: Wie kann man im Browser prüfen, ob das CSS geladen wurde? (Tipp: Entwicklertools)

---

## Schritt 4 – Schreibe erste CSS-Regeln

Wie du siehst ist die Struktur einer CSS Regel folgendermaßen:

```css

selektor {
    Attribut1: Wert;
    Attribut2: Wert;
}
```

oder in echt:

```css
body {
    background: blue;
}

```

Achte auf die `{}` und das `;` nach einem Wert. Sonst könnten schlechte Dinge passieren.


Fang an zu experimentieren. Füge in `scoreboard.css` ein paar Styling Regeln ein. Dabei gibt es keine Vorgabe. Überlege was du verändern möchtest (erst noch einfache Dinge bitte)
und suche nach passenden CSS Attributen. Farbbezeichnungen findest du z.B. hier [Farbcodes](https://htmlcolorcodes.com/color-names/)

Wenn du genug experimentiert hast, füge in `scoreboard.css` folgende Regeln ein und lies die Kommentare. Tipp: Wenn du keinen zentrierten weißen Container siehst, überlege ob dein CSS-Code zu deinem HTML-Code passt (Stichwort Klassen-Selektor).

```css
body {
    background: #232526;
    color: #e0e0e0;
    font-family: 'Segoe UI', Arial, sans-serif;
    margin: 0;
    padding: 0;
}
.scoreboard-wrapper {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 24px #0004;
    max-width: 400px;
    margin: 3em auto;
    padding: 2em 2em 1em 2em;
    text-align: center;
}
```

**Erklärung:**
- `background`: Hintergrundfarbe
- `color`: Textfarbe
- `font-family`: Schriftart (erste Wahl, dann Alternativen)
- `margin`/`padding`: Außen- und Innenabstand
- `border-radius`: Abgerundete Ecken
- `box-shadow`: Schatten

### Aufgabe:
- Ändere die Hintergrundfarbe des Bodys auf eine Farbe deiner Wahl (z.B. mit [color-hex.com](https://www.color-hex.com/)).
- Probiere eine andere Schriftart aus (z.B. `monospace`).

---

## Schritt 5 – Teste deine Seite

Speichere beide Dateien und öffne `scoreboard.html` im Browser. Du solltest jetzt einen modernen, zentrierten Container sehen.

---

