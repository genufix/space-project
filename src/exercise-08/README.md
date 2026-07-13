# Optional - Übung 8 – Theme-Toggle mit mehreren Themes (light, dark, futuristic)

In dieser Übung lernst du, wie du einen Theme-Toggle-Button baust, mit dem du zwischen mehreren Themes (z.B. light, dark, futuristic) umschalten kannst. Du nutzt CSS-Variablen für die verschiedenen Themes und setzt das Theme über ein Attribut am `<body>`.

---

## Schritt 1 – Was sind data-Attribute und wie funktionieren sie?

Mit sogenannten **data-Attributen** kannst du eigene Informationen an HTML-Elemente hängen. Im Projekt wird das Attribut `data-theme` am `<body>` genutzt, um das aktuelle Theme zu speichern.

Beispiel:
```html
<body data-theme="light">
```
Im CSS kannst du dann gezielt für verschiedene Themes Variablen überschreiben:
```css
body[data-theme="dark"] {
    --main-bg: ...;
    /* ... */
}
```

### Aufgabe 1:
- Füge im HTML das Attribut `data-theme="light"` zum `<body>` hinzu.
- Erkläre, wie Attribut-Selektoren in CSS funktionieren.
- Probiere im Dev-Tool aus, wie du das Attribut änderst und wie sich das Aussehen verändert.

---

## Schritt 2 – CSS-Variablen für alle Themes

Im Projekt werden die Farben und Styles für jedes Theme über CSS-Variablen geregelt. Im :root stehen die Standardwerte (light), für dark und futuristic werden sie überschrieben:

Beispiel:
```css
:root {
    --main-bg: #f5f7fa;
    --panel-bg: #fff;
    --accent: #1a8cff;
    --text-color: #232526;
}
body[data-theme="dark"] {
    --main-bg: linear-gradient(120deg, #232526, #414345);
    --panel-bg: #232526;
    --accent: #ff4081;
    --text-color: #fff;
}
body[data-theme="futuristic"] {
    --main-bg: linear-gradient(120deg, #0f2027, #2c5364);
    --panel-bg: #181c25;
    --accent: #00ffe7;
    --text-color: #fff;
}
```

### Aufgabe 2:
- Schreibe eigene Variablen für ein viertes Theme (z.B. "retro") und probiere es aus.
- Erkläre, wie das Überschreiben der Variablen funktioniert.
- Was passiert, wenn du eine Variable im Theme vergisst?

---

## Schritt 3 – Theme-Toggle-Button im HTML

Füge in dein HTML einen Button ein, mit dem das Theme gewechselt werden kann. Aus dieser Div machen wir später einen Button:
```html
    <div id="theme-toggle" class="theme-toggle">🌗 Switch Theme</div>
```

### Aufgabe 3:
- Benenne den Button um oder ändere den Text per JavaScript.
- Erkläre, wie du den Button im DOM auswählst.

## Schritt 3a – Event-Handler für den Theme-Toggle-Button

Damit beim Klick auf den Theme-Toggle-Button später wirklich etwas passiert, musst du einen sogenannten **Event-Handler** registrieren. Ein Event-Handler ist eine Funktion, die auf ein bestimmtes Ereignis (z.B. einen Klick) reagiert.

### Aufgabe 3a:
- Nutze folgenden Einstieg in deinem JavaScript:
  ```js
  window.addEventListener('DOMContentLoaded', function() {
      var toggle = document.getElementById('theme-toggle');
      // ...
  });
  ```
- Überlege: Wie kannst du dafür sorgen, dass beim Klick auf den Button eine Funktion ausgeführt wird? (Stichwort: Event-Handler). Recherchiere dafür im Browser.
- Implementiere einen Event-Handler, der beim Klick auf den Button eine Test-Nachricht in der Konsole ausgibt.
- Teste im Browser, ob deine Lösung funktioniert.
- Reflektiere: Warum ist dieser Event-Handler nötig? Was würde ohne ihn passieren?

**Hinweis:**  
Der Event-Handler ist die Verbindung zwischen dem UI (Button) und deiner Logik. Ohne ihn würde beim Klick auf den Button nichts passieren – der Button wäre nur Deko!

---

## Schritt 4 – Theme-Logik in JavaScript
Im Projekt gibt es ein Array mit allen Themes und eine Funktion, die das Theme setzt. Beim Klick auf den Button wird das nächste Theme ausgewählt und als `data-theme` gesetzt.

**Wichtige Syntax-Erklärung:**
- `setAttribute('data-theme', theme)` setzt das Attribut am `<body>`.
- `currentThemeIdx = (currentThemeIdx + 1) % THEMES.length;` sorgt dafür, dass nach dem letzten Theme wieder das erste kommt (Kreis).

Beispiel (wie im Projekt):
```js
const THEMES = ['light', 'dark', 'futuristic'];
let currentThemeIdx = 0;
function setTheme(theme) {
    document.body.setAttribute('data-theme', theme);
}
```

---

## Schritt 5 – Die Funktion cycleTheme

Im Projekt gibt es zusätzlich die Funktion `cycleTheme`, die das Theme zyklisch durchschaltet. Sie ist besonders praktisch, wenn du die Logik an mehreren Stellen nutzen willst (z.B. für verschiedene Buttons oder Tastenkombinationen).

**Original aus scoreboard.js:**
```js
function cycleTheme() {
    currentThemeIdx = (currentThemeIdx + 1) % THEMES.length;
    setTheme(xxx);
}
```

**Erklärung:**
- `cycleTheme` erhöht den Index und ruft dann `setTheme` mit dem neuen Theme auf.
- Sie ist von der Event-Logik getrennt und kann überall wiederverwendet werden.

### Aufgabe 4:
- Ersetze in der Funktion cycleTheme() das "xxx" durch korrekten Code.
- Ersetze im Event-Handler die anonyme Funktion durch einen Aufruf von `cycleTheme`.
- Überlege, warum es sinnvoll ist, die Logik in eine eigene Funktion auszulagern.
- Baue einen Test ein: Was passiert, wenn du cycleTheme mehrfach hintereinander aufrufst?

---

## Schritt 6 – Mini-Experimente & Verständnisfragen
- Was passiert, wenn du ein Theme entfernst oder hinzufügst?
- Wie kannst du den aktuellen Theme-Namen im UI anzeigen?
- Wie würdest du das Theme automatisch nach Tageszeit wählen?

---

## Komplette Lösung

<details>
<summary>Hier klicken, um die Lösung anzuzeigen</summary>

**HTML (Ausschnitt):**
```html
    <div id="theme-toggle" class="theme-toggle">🌗 Switch Theme</div>
```

**JavaScript (Ausschnitt):**
```js
var THEMES = ['light', 'dark', 'futuristic'];
var currentThemeIdx = 0;
function setTheme(theme) {
    document.body.setAttribute('data-theme', theme);
}
function cycleTheme() {
    currentThemeIdx = (currentThemeIdx + 1) % THEMES.length;
    setTheme(THEMES[currentThemeIdx]);
}
window.addEventListener('DOMContentLoaded', function() {
    setTheme(THEMES[0]);
    var toggle = document.getElementById('theme-toggle');
    if (toggle) toggle.onclick = cycleTheme;
});
```

**CSS (Ausschnitt):**
```css
:root {
    --main-bg: linear-gradient(120deg, #232526, #414345);
    --panel-bg: rgba(255, 255, 255, 0.95);
    --text-color: #232526;
    --accent: #1a8cff;
}
body[data-theme='dark'] {
    --main-bg: linear-gradient(120deg, #0f2027, #2c5364);
    --panel-bg: rgba(30, 34, 44, 0.98);
    --text-color: #e0e0e0;
    --accent: #00bfff;
}
body[data-theme='futuristic'] {
    --main-bg: radial-gradient(ellipse at top, #0fffc3 0%, #3a3a52 100%);
    --panel-bg: rgba(20, 30, 40, 0.98);
    --text-color: #fff;
    --accent: #ff00ea;
}
```
</details> 
