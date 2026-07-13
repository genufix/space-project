# Optional - Übung 9 – Top-Score-Anzeige mit Glow-Effekt und animiertem Digitalzähler

In dieser Übung lernst du, wie du die Top-Score-Anzeige mit Glow-Effekt und animiertem Digitalzähler wie im echten Projekt umsetzt. Du verstehst, wie HTML, CSS und JavaScript zusammenarbeiten, um die Animation und die Glückwunsch-Nachricht anzuzeigen. Der Lösungs-Code entspricht exakt dem aus scoreboard.js.

---

## Schritt 1 – HTML-Struktur für die Top-Score-Anzeige

Im Projekt gibt es einen speziellen Bereich für den Top-Score und die Glückwunsch-Nachricht. Die wichtigsten Elemente sind:
```html
<div id="top-score-counter-container" class="top-score-counter-container">
    <div class="top-score-counter-label">Top Score</div>
    <div id="top-score-counter" class="top-score-counter">0</div>
    <div id="top-score-congrats" class="top-score-congrats hidden"></div>
</div>
```
- `top-score-counter`: Zeigt den animierten Score an.
- `top-score-congrats`: Zeigt die Glückwunsch-Nachricht an.

### Aufgabe 1:
- Baue die HTML-Struktur in deine Seite ein.
- Erkläre, wofür die einzelnen IDs und Klassen genutzt werden.
- **Erweitere die Struktur:** Füge ein weiteres Element hinzu, z.B. für ein Icon oder einen Untertitel, und style es passend.

---

## Schritt 2 – CSS für Glow-Effekt und Digitalzähler

Im Projekt werden für die Top-Score-Anzeige spezielle Styles verwendet:
- Glow-Effekt mit `box-shadow` und animiertem Farbverlauf.
- Digitale Schriftart und Animationen.

Beispiel:
```css
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

### Aufgabe 2:
- Übernehme die CSS-Styles und experimentiere mit anderen Farben oder Schatten.
- Erkläre, wie der Glow-Effekt entsteht.
- Was bewirkt die Klasse `hidden`?
- **Schreibe eine eigene CSS-Animation** (z.B. ein leichtes Pulsieren oder Farbwechsel für den Digitalzähler) und binde sie ein.

---

## Schritt 3 – JavaScript: Animierter Digitalzähler und Glückwunsch

Im Projekt wird der Top-Score mit einer Tipp- und Lösch-Animation angezeigt. Die wichtigsten Funktionen sind:
- `animateTopScoreTyping(scoreStr)`: Zeigt den Score wie beim Tippen an.
- `animateTopScoreDeleting(scoreStr)`: Löscht den Score wie beim Rückwärts-Tippen.
- `updateTopScoreCounter(scores)`: Steuert die Animation und zeigt die Glückwunsch-Nachricht an.

**Original aus scoreboard.js:**
```js
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
            typingTimeout = setTimeout(typeNext, 180); // langsames Tippen
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreDeleting(scoreStr);
            }, 1800); // Pause vor dem Löschen
        }
    }
    typeNext();
}

// TODO: Praktikanten-Aufgabe: Implementiere animateTopScoreDeleting selbst!

function updateTopScoreCounter(scores) {
    var counter = document.getElementById('top-score-counter');
    var congrats = document.getElementById('top-score-congrats');
    var topScore = (scores && scores.length > 0) ? scores[0].score : 0;
    var topPlayer = (scores && scores.length > 0) ? scores[0].player : null;
    var toStr = String(topScore);

    // Wenn sich der Score ändert, Animation neu starten
    if (toStr !== String(lastTopScore)) {
        if (typingTimeout) clearTimeout(typingTimeout);
        animateTopScoreTyping(toStr);
    }
    lastTopScore = topScore;

    // Glückwunsch-Nachricht anzeigen/verstecken
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
```

**Erklärung:**
- Die Animation wird mit `setTimeout` Schritt für Schritt erzeugt.
- Die Glückwunsch-Nachricht wird je nach Top-Player angezeigt oder versteckt.

### Aufgabe 3:
- **Implementiere die Funktion `animateTopScoreDeleting(scoreStr)` selbst!**
    - Tipp: Sie funktioniert ähnlich wie `animateTopScoreTyping`, aber löscht von rechts nach links.
    - Nutze `setTimeout` und `textContent`.
- Erkläre, wie die Tipp- und Lösch-Animation funktioniert.
- Probiere verschiedene Werte für die Pausen und Geschwindigkeiten aus.
- **Passe die Glückwunsch-Nachricht an:** Zeige z.B. den Score mit an oder schreibe eine eigene Nachricht.
- **Experimentiere:** Baue einen Button ein, mit dem du die Animation manuell starten oder stoppen kannst.
- **Aufgabe:** Damit der Topscorrer beim Laden der Seite direkt angezeigt wird, sollte der Methodenaufruf für die TopScoreAnzeige auch in der Funktion renderScoreboard aufgerufen werden. Füge das ein!

---

## Schritt 4 – Mini-Experimente & Verständnisfragen
- Wie würdest du die Animation anhalten, wenn der Nutzer die Seite verlässt?
- Wie kannst du die Glückwunsch-Nachricht individuell gestalten?
- Wie würdest du die Animation für sehr große Zahlen anpassen?
- **Bonus:** Schreibe eine Funktion, die die Animation rückwärts ablaufen lässt (erst löschen, dann tippen).

---

## Komplette Lösung

<details>
<summary>Hier klicken, um die Lösung anzuzeigen</summary>

**HTML (Ausschnitt):**
```html
<div id="top-score-counter-container" class="top-score-counter-container">
    <div class="top-score-counter-label">Top Score</div>
    <div id="top-score-counter" class="top-score-counter">0</div>
    <div id="top-score-congrats" class="top-score-congrats hidden"></div>
</div>
```

**CSS (Ausschnitt):**
```css
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

**JavaScript (Ausschnitt):**
```js
function animateTopScoreTyping(scoreStr) {
    var counter = document.getElementById('top-score-counter');
    var i = 0;
    typingState = 'typing';
    function typeNext() {
        counter.textContent = scoreStr.slice(0, i);
        if (i < scoreStr.length) {
            i++;
            typingTimeout = setTimeout(typeNext, 180);
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreDeleting(scoreStr);
            }, 1800);
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
            typingTimeout = setTimeout(deleteNext, 120);
        } else {
            typingState = 'idle';
            typingTimeout = setTimeout(function() {
                animateTopScoreTyping(scoreStr);
            }, 1200);
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
    if (toStr !== String(lastTopScore)) {
        if (typingTimeout) clearTimeout(typingTimeout);
        animateTopScoreTyping(toStr);
    }
    lastTopScore = topScore;
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
```

</details> 
