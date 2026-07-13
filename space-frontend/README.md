# Optional - Übung 11 – Feinschliff, Footer, Animationen, Projektabschluss

In dieser letzten Übung bringst du dein Scoreboard auf das Niveau des echten Projekts: Du baust einen Footer ein, prüfst die Responsivität, ergänzt letzte Animationen und räumst den Code auf. Außerdem kannst du eigene Experimente machen und das Projekt kreativ abschließen.

---

## Schritt 1 – Footer einbauen

Auf den meisten Websiten gibt es einen Footer am unteren Rand des Scoreboards:
```html
<footer class="footer">&copy; 2025 Space Project &mdash; Powered by genua</footer>
```
- Der Footer steht innerhalb des Scoreboard-Containers.

### Aufgabe 1:
- Baue den Footer wie oben in dein HTML ein.
- Ändere den Text und das Jahr testweise ab.
- **Experimentiere:** Baue einen Link oder ein Icon in den Footer ein.

---

## Schritt 2 – Footer und Feinschliff im CSS

Im Projekt ist der Footer dezent und responsiv gestaltet:
```css
.footer {
    margin-top: 2rem;
    font-size: 0.95rem;
    color: #888;
    border-top: 1px solid #e0e0e0;
    padding-top: 1rem;
    background: transparent;
}
```
- Der Footer hat einen Abstand nach oben, eine kleinere Schrift und eine dezente Farbe.

### Aufgabe 2:
- Übernehme die CSS-Styles für den Footer.
- Passe die Farbe oder den Abstand an.
- **Programmieraufgabe:** Baue eine kleine Animation ein, z.B. dass der Footer beim Laden leicht einblendet.

---

## Schritt 3 – Letzte Animationen und Details

Damit die Website eleganter für den User aussieht gibt es verschiedene Animationen, z.B. für die Scoreboard-Umrandung, den Top-Score und die Glückwunsch-Nachricht. Beispiele:

**Was sind @keyframes?**
`@keyframes` definiert eine CSS-Animation. Du gibst an, wie sich ein Element zu verschiedenen Zeitpunkten (0%, 50%, 100%) verhalten soll. Der Browser interpoliert dann automatisch die Zwischenwerte.

```css
.scoreboard-wrapper {
    animation: border-glow 2.5s infinite alternate;
}
@keyframes border-glow {
    0% { box-shadow: 0 4px 32px 0 #0008, 0 0 0 4px var(--accent); }
    100% { box-shadow: 0 8px 48px 8px var(--accent), 0 0 0 8px var(--accent); }
}
.top-score-counter {
    animation: counter-glow 1.5s infinite alternate, counter-pulse 2.2s infinite;
}
@keyframes counter-glow {
    0% { box-shadow: 0 0 32px 4px var(--accent), 0 0 64px 16px var(--accent)44; }
    100% { box-shadow: 0 0 64px 16px var(--accent), 0 0 128px 32px var(--accent)44; }
}
@keyframes counter-pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.08); }
}
```

### Aufgabe 3:
- Übernehme die Animationen für Scoreboard, Top-Score und Footer.
- **Experimentiere:** Passe die Dauer oder Intensität der Animationen an.
- Baue eine eigene kleine Animation ein (z.B. ein Icon, das pulsiert).

---

## Schritt 4 – Responsive-Check und Media Queries

Im Projekt wird das Layout mit Media Queries responsiv gemacht. Damit kann sich die Website automatisch auf verschiedene Bildschirmgrößen anpassen:
```css
@media (max-width: 600px) {
    .scoreboard-wrapper {
        padding: 1em 0.5em;
    }
    table, th, td {
        font-size: 0.95em;
    }
}
@media (min-width: 601px) and (max-width: 900px) {
    .scoreboard-wrapper {
        max-width: 90vw;
    }
}
```

### Aufgabe 4:
- Überprüfe dein Scoreboard auf verschiedenen Bildschirmgrößen (z.B. mit dem Browser-Dev-Tool).
- Schreibe eine eigene Media Query, die das Layout für Tablets oder Smartphones anpasst.
- **Programmieraufgabe:** Baue einen Button ein, der die aktuelle Fensterbreite anzeigt.

---

## Schritt 5 – Aufräumen und Projektabschluss

Bei der Entwicklung von Software wird der Code am Ende aufgeräumt:
- Unnötige Kommentare und Test-Code werden entfernt.
- Alle Dateien werden noch einmal überprüft.
- Die wichtigsten Funktionen und Styles sind dokumentiert.

### Aufgabe 5:
- Entferne nicht mehr benötigte Zeilen und Kommentare aus deinem Code.
- Schreibe kurze Kommentare zu den wichtigsten Funktionen.
- **Experimentiere:** Schreibe eine eigene kleine Doku oder ein README für dein fertiges Projekt.

---

## Schritt 6 – Eigene Experimente und kreative Erweiterungen
- Baue ein eigenes Feature ein (z.B. Easter Egg).
- Schreibe eine kleine Anleitung, wie man das Projekt startet oder erweitert.
- **Programmieraufgabe:** Baue einen Button ein, der ein zufälliges Theme auswählt.

## Finaler Schritt 7 – Einbindung der Websockets

Wenn du und alle anderen Gruppen fertig sind, dann könnt ihr eure Projekte endlich zusammenführen. Diesen Schritt werden wir alle gemeinsam machen. Dafür müsstest du in deiner HTML-Datei statt "scoreboard-ws.js" die Datei "scoreboard-ws-realtime.js" verwenden und diese Datei in deinen Ordner verschieben.

---

## Komplette Lösung (Finale Projektlösung)

<details>
<summary>Hier klicken, um die Lösung anzuzeigen</summary>

**scoreboard.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space Game Scoreboard</title>
    <!-- Main stylesheet for scoreboard -->
    <link rel="stylesheet" href="scoreboard.css">
</head>
<body>
    <!-- Animated star background -->
    <div id="star-bg"></div>
    <!-- Scoreboard container with animated border -->
    <div class="scoreboard-wrapper futuristic-border" id="scoreboard-container">
        <h1>🚀 Space Game Scoreboard</h1>
        <p class="description">See the top 10 players and their scores. The scoreboard updates in real-time.<br>Experiment with the theme toggle and discover fun facts!</p>
        <div id="theme-toggle" class="theme-toggle">🌗 Switch Theme</div>
        <div id="refresh-indicator" class="refresh-indicator">Last updated: <span id="last-updated">-</span></div>
        <!-- Animated digital counter for top score -->
        <div id="top-score-counter-container" class="top-score-counter-container">
            <div class="top-score-counter-label">Top Score</div>
            <div id="top-score-counter" class="top-score-counter">0</div>
            <div id="top-score-congrats" class="top-score-congrats hidden"></div>
        </div>
        <table id="scoreboard">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Player</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>
                <!-- Scores will be populated here by scoreboard.js -->
            </tbody>
        </table>
        <div id="error-message" class="hidden"></div>
        <footer class="footer">&copy; 2025 Space Project &mdash; Powered by genua</footer>
    </div>
    <!-- Main JS for rendering scoreboard -->
    <script src="scoreboard.js"></script>
    <!-- WebSocket logic for real-time updates -->
    <script src="scoreboard-ws.js"></script>
</body>
</html> 
```

**scoreboard.css**
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
body {
    background: var(--main-bg);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-color);
    transition: background 0.8s, color 0.5s;
}

/* Animated star background */
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

/* Scoreboard container with glowing border */
.scoreboard-wrapper {
    background: var(--panel-bg);
    border-radius: 20px;
    box-shadow: 0 4px 32px 0 #0008, 0 0 0 4px var(--accent);
    padding: 2.5rem 2.5rem 2rem 2.5rem;
    max-width: 480px;
    width: 100%;
    text-align: center;
    position: relative;
    z-index: 1;
    border: 2px solid var(--accent);
    animation: border-glow 2.5s infinite alternate;
}
@keyframes border-glow {
    0% { box-shadow: 0 4px 32px 0 #0008, 0 0 0 4px var(--accent); }
    100% { box-shadow: 0 8px 48px 8px var(--accent), 0 0 0 8px var(--accent); }
}

h1 {
    margin-bottom: 1.2rem;
    color: var(--accent);
    font-size: 2.2rem;
    letter-spacing: 2px;
    text-shadow: 0 0 8px var(--accent), 0 0 32px #fff2;
}

.theme-toggle {
    display: inline-block;
    background: var(--accent);
    color: #fff;
    border-radius: 20px;
    padding: 0.4em 1.2em;
    margin-bottom: 1.2em;
    margin-top: 0.5em;
    font-weight: 600;
    font-size: 1.1em;
    cursor: pointer;
    box-shadow: 0 2px 12px 0 var(--accent);
    transition: background 0.3s, color 0.3s;
    user-select: none;
}
.theme-toggle:hover {
    background: #fff;
    color: var(--accent);
}

/* Scoreboard table styles */
table#scoreboard {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1rem;
    background: transparent;
}
table#scoreboard th, table#scoreboard td {
    padding: 0.75rem 0.5rem;
    border-bottom: 1px solid #e0e0e0;
    background: transparent;
}
table#scoreboard th {
    background: var(--accent);
    color: #fff;
    font-weight: 600;
    text-shadow: 0 0 8px #0008;
}
table#scoreboard tbody tr:nth-child(even) {
    background: #f7f7f733;
}
table#scoreboard tbody tr:hover {
    background: #e3e9f799;
}

/* Error message styling */
#error-message {
    color: #b00020;
    margin-top: 1rem;
    font-size: 1rem;
}

.hidden {
    display: none;
}

.description {
    color: var(--text-color);
    font-size: 1.05rem;
    margin-bottom: 0.5rem;
}

.refresh-indicator {
    font-size: 0.95rem;
    color: #666;
    margin-bottom: 1rem;
}

.footer {
    margin-top: 2rem;
    font-size: 0.95rem;
    color: #888;
    border-top: 1px solid #e0e0e0;
    padding-top: 1rem;
    background: transparent;
}

/* --- Animated Digital Counter for Top Score --- */
.top-score-counter-container {
    margin-bottom: 1.5rem;
    text-align: center;
    width: 100%;
    position: relative;
}
.top-score-counter-label {
    color: var(--accent);
    font-size: 1.1em;
    font-weight: bold;
    margin-bottom: 0.3em;
    letter-spacing: 1px;
    text-shadow: 0 0 8px var(--accent), 0 0 16px #fff2;
}
.top-score-counter {
    font-family: 'Orbitron', 'Consolas', 'Courier New', monospace;
    font-size: 2.8em;
    color: var(--accent);
    background: #000a;
    border-radius: 16px;
    padding: 0.2em 0.7em;
    box-shadow: 0 0 32px 4px var(--accent), 0 0 64px 16px var(--accent)44;
    text-shadow: 0 0 24px var(--accent), 0 0 48px #fff2;
    letter-spacing: 0.08em;
    margin: 0 auto 0.2em auto;
    display: inline-block;
    border: 3px solid var(--accent);
    transition: color 0.3s, background 0.3s, border 0.3s;
    animation: counter-glow 1.5s infinite alternate, counter-pulse 2.2s infinite;
    position: relative;
    z-index: 1;
    min-width: 3.2em;
    min-height: 1em;
    text-align: center;
}
@keyframes counter-glow {
    0% { box-shadow: 0 0 32px 4px var(--accent), 0 0 64px 16px var(--accent)44; }
    100% { box-shadow: 0 0 64px 16px var(--accent), 0 0 128px 32px var(--accent)44; }
}
@keyframes counter-pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.08); }
}
.top-score-congrats {
    margin-top: 0.5em;
    font-size: 1.15em;
    color: var(--accent);
    font-family: 'Orbitron', 'Consolas', 'Courier New', monospace;
    text-shadow: 0 0 12px var(--accent), 0 0 32px #fff2;
    letter-spacing: 0.04em;
    opacity: 0;
    transform: translateY(10px) scale(0.98);
    transition: opacity 0.5s, transform 0.5s;
    pointer-events: none;
}
.top-score-congrats.visible {
    opacity: 1;
    transform: translateY(0) scale(1.04);
    animation: congrats-flicker 1.2s infinite alternate;
}
@keyframes congrats-flicker {
    0% { text-shadow: 0 0 12px var(--accent), 0 0 32px #fff2; }
    100% { text-shadow: 0 0 24px var(--accent), 0 0 64px #fff2; }
}
```

**scoreboard.js**
```js
// scoreboard.js
// Contains rendering and helper functions for the scoreboard.
// WebSocket logic is now in scoreboard-ws.js

// Updates the animated digital counter for the top score and congratulates the top player
var lastTopScore = 0;
var typingInterval = null;
var typingState = 'idle'; // 'typing', 'deleting', 'idle'
var typingTimeout = null;

function animateTopScoreTyping(scoreStr) {
    var counter = document.getElementById('top-score-counter');
    var i = 0;
    typingState = 'typing';
    function typeNext() {
        counter.textContent = scoreStr.slice(0, i);
        if (i < scoreStr.length) {
            i++;
            typingTimeout = setTimeout(typeNext, 180); // slower typing
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreDeleting(scoreStr);
            }, 1800); // pause before deleting
        }
    }
    typeNext();
}

function animateTopScoreDeleting(scoreStr) {
    var counter = document.getElementById('top-score-counter');
    var i = scoreStr.length;
    typingState = 'deleting';
    function deleteNext() {
        counter.textContent = scoreStr.slice(0, i);
        if (i > 0) {
            i--;
            typingTimeout = setTimeout(deleteNext, 120); // slower deleting
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreTyping(scoreStr);
            }, 1200); // pause before re-typing
        }
    }
    deleteNext();
}

function updateTopScoreCounter(scores) {
    var counter = document.getElementById('top-score-counter');
    var congrats = document.getElementById('top-score-congrats');
    var topScore = (scores && scores.length > 0) ? scores[0].score : 0;
    var topPlayer = (scores && scores.length > 0) ? scores[0].player : null;
    var toStr = String(topScore);

    // If the score changed, restart the animation
    if (toStr !== String(lastTopScore)) {
        if (typingTimeout) clearTimeout(typingTimeout);
        animateTopScoreTyping(toStr);
    }
    lastTopScore = topScore;

    // Show/hide congratulation message
    if (topPlayer) {
        congrats.textContent = 'Congratulations, ' + topPlayer + '!';
        congrats.classList.remove('hidden');
        congrats.classList.add('visible');
    } else {
        congrats.textContent = '';
        congrats.classList.add('hidden');
        congrats.classList.remove('visible');
    }
}

// Renders the scoreboard table with the top 10 scores
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
            '<td>' + entry.player + '</td>' +
            '<td>' + entry.score + '</td>';
        tbody.appendChild(tr);
    }
    updateTopScoreCounter(topScores);
}

// Show error message
function showError(message) {
    var errorDiv = document.getElementById('error-message');
    errorDiv.textContent = message;
    errorDiv.classList.remove('hidden');
}

// Updates the last updated time
function updateRefreshIndicator() {
    var now = new Date();
    var formatted = now.toLocaleTimeString();
    document.getElementById('last-updated').textContent = formatted;
}

// Creates a simple animated star background
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

// Theme toggle: cycles through three themes
var THEMES = ['light', 'dark', 'futuristic'];
var currentThemeIdx = 0;
function setTheme(theme) {
    document.body.setAttribute('data-theme', theme);
}
function cycleTheme() {
    currentThemeIdx = (currentThemeIdx + 1) % THEMES.length;
    setTheme(THEMES[currentThemeIdx]);
}

// Set up everything when the page loads
window.addEventListener('DOMContentLoaded', function() {
    setTheme(THEMES[0]);
    var toggle = document.getElementById('theme-toggle');
    if (toggle) toggle.onclick = cycleTheme;
    createStars(80);
}); 
```
</details> 
