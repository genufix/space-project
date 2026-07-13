# Optional - Übung 10 – Animierter Sternenhintergrund

In dieser Übung lernst du, wie du einen animierten Sternenhintergrund wie im echten Projekt umsetzt. Du verstehst, wie HTML, CSS und JavaScript zusammenarbeiten, um viele kleine Sterne zufällig zu platzieren und zu animieren. Der Lösungs-Code entspricht exakt dem aus scoreboard.js.

---

## Schritt 1 – HTML-Struktur für den Sternenhintergrund

Im Projekt gibt es ein eigenes Element für den Sternenhintergrund:
```html
<div id="star-bg"></div>
```
- Dieses Element liegt meist ganz oben im `<body>` und wird per CSS und JS mit Sternen gefüllt.

### Aufgabe 1:
- Baue das Element `<div id="star-bg"></div>` in deine Seite ein.
- Erkläre, warum es sinnvoll ist, den Sternenhintergrund in ein eigenes Element zu packen.
- **Experimentiere:** Füge ein weiteres Hintergrund-Element ein und vergleiche die Effekte.
- **Programmieraufgabe:** Baue einen Button in dein HTML ein, mit dem du die Sterne neu generieren kannst.

---

## Schritt 2 – CSS für den Sternenhintergrund und die Sterne

Im Projekt werden die Sterne absolut positioniert und mit einer Animation versehen. Die wichtigsten Styles sind:
```css
#star-bg {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: 0;
    pointer-events: none;
    width: 100vw; height: 100vh;
    overflow: hidden;
}
.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    box-shadow: 0 0 6px 2px #fff, 0 0 12px 4px #1a8cff44;
    pointer-events: none;
    will-change: transform;
    animation: twinkle 2s infinite alternate;
}
@keyframes twinkle {
    0% { opacity: 0.6; }
    100% { opacity: 1; }
}
```
- `width: 100vw; height: 100vh;` sorgt dafür, dass der Sternenhintergrund immer die ganze Viewport-Fläche abdeckt.
- `.star` hat jetzt einen komplexeren `box-shadow` für einen bläulichen Glow.
- `pointer-events: none;` sorgt dafür, dass die Sterne keine Mausereignisse blockieren.
- `will-change: transform;` gibt dem Browser einen Hinweis für bessere Performance bei Animationen.
- `animation: twinkle 2s infinite alternate;` sorgt für ein sanftes Leuchten (statt linearem Loop).
- Die Animation geht jetzt von `opacity: 0.6` zu `opacity: 1`.

### Aufgabe 2:
- Übernehme die CSS-Styles und experimentiere mit anderen Farben, Größen oder Animationen.
- Erkläre, wie absolute Positionierung und Animationen funktionieren.
- **Programmieraufgabe:** Schreibe eine eigene Animation (z.B. Farbwechsel oder Bewegung) und binde sie für einzelne Sterne ein.
- **Experimentiere:** Entferne testweise `pointer-events: none;` oder ändere `will-change` und beobachte die Auswirkungen.

---

## Schritt 3 – JavaScript: Sterne erzeugen und animieren

Im Projekt werden die Sterne per JavaScript erzeugt und zufällig positioniert. Die zentrale Funktion ist:

**Original aus scoreboard.js:**
```js
function createStars(numStars) {
    var starBg = document.getElementById('star-bg');
    if (!starBg) return;
    starBg.innerHTML = '';
    for (var i = 0; i < numStars; i++) {
        var star = document.createElement('div');
        star.className = 'star';
        var size = Math.random() * 2 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.top = (Math.random() * 100) + '%';
        star.style.left = (Math.random() * 100) + '%';
        star.style.animationDuration = (2 + Math.random() * 4) + 's';
        starBg.appendChild(star);
    }
}
```
- Mit `createElement('div')` wird ein neues Stern-Element erzeugt.
- Mit `Math.random()` werden Größe, Position und Animationsdauer zufällig gewählt.
- Mit `appendChild` wird der Stern zum Hintergrund hinzugefügt.

### Aufgabe 3:
- **Schreibe die Funktion `createStars(numStars)` Schritt für Schritt selbst!**
    - Erzeuge für eine beliebige Zahl von Sternen die Elemente und setze zufällige Werte.
    - Erkläre, wie `Math.random()` und `appendChild` funktionieren.
- **Programmieraufgabe:** Schreibe eine Funktion, die alle Sterne entfernt (z.B. `clearStars()`).
- **Programmieraufgabe:** Baue den Button aus Aufgabe 1 so um, dass er beim Klick die Sterne neu generiert (nutze `createStars`).
- Probiere verschiedene Werte für die Anzahl der Sterne, Größen und Animationsdauern aus.
- **Bonus:** Erzeuge Sterne in verschiedenen Farben oder mit unterschiedlichen Animationen.

---

## Schritt 4 – Mini-Experimente & Verständnisfragen
- Was passiert, wenn du das Fenster verkleinerst oder vergrößerst?
- Wie würdest du die Sterne beim Scrollen oder bei Fenstergröße neu anordnen?
- Wie kannst du die Performance verbessern, wenn sehr viele Sterne angezeigt werden?
- **Programmieraufgabe:** Baue einen "Sternschnuppen"-Effekt ein (Sterne, die sich bewegen und verschwinden).
- **Programmieraufgabe:** Schreibe eine Funktion, die die Anzahl der Sterne dynamisch an die Fenstergröße anpasst.
- Füge den Methodenaufruf der createStarts- Methode in den Eventlistener in scoreboars.js ein, sodass die Sterne direkt beim Laden da sind.

---

## Komplette Lösung

<details>
<summary>Hier klicken, um die Lösung anzuzeigen</summary>

**HTML (Ausschnitt):**
```html
<div id="star-bg"></div>
```

**CSS (Ausschnitt):**
```css
#star-bg {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: 0;
    pointer-events: none;
    width: 100vw; height: 100vh;
    overflow: hidden;
}
.star {
    position: absolute;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    box-shadow: 0 0 6px 2px #fff, 0 0 12px 4px #1a8cff44;
    pointer-events: none;
    will-change: transform;
    animation: twinkle 2s infinite alternate;
}
@keyframes twinkle {
    0% { opacity: 0.6; }
    100% { opacity: 1; }
}
```

**JavaScript (Ausschnitt):**
```js
function createStars(numStars) {
    var starBg = document.getElementById('star-bg');
    if (!starBg) return;
    starBg.innerHTML = '';
    for (var i = 0; i < numStars; i++) {
        var star = document.createElement('div');
        star.className = 'star';
        var size = Math.random() * 2 + 1;
        star.style.width = size + 'px';
        star.style.height = size + 'px';
        star.style.top = (Math.random() * 100) + '%';
        star.style.left = (Math.random() * 100) + '%';
        star.style.animationDuration = (2 + Math.random() * 4) + 's';
        starBg.appendChild(star);
    }
}
```
</details> 
