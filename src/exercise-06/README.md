# Übung 6 – Moderne Styles und Responsive-Design

In dieser Übung lernst du, wie du das Scoreboard mit modernen CSS-Features und Responsive-Design gestaltest. Du verstehst, wie CSS-Variablen, Selektoren, Vererbung, Kaskade und Media Queries funktionieren und wie du sie gezielt einsetzt.

---

## Schritt 1 – CSS-Variablen und :root

CSS-Variablen (Custom Properties) machen es einfach, Farben und andere Werte zentral zu verwalten. Sie werden im `:root`-Block (ganz oben im CSS) definiert und mit `var(--name)` verwendet.

Beispiel:
```css
:root {
    --main-bg: linear-gradient(120deg, #232526, #414345);
    --panel-bg: #fff;
    --accent: #1a8cff;
    --text-color: #232526;
}
```

### Aufgabe 1:
- Lege eigene Variablen für z.B. Schatten, weitere Farben oder Abstände an und verwende sie im Layout.
- Erkläre, warum Variablen im `:root`-Block stehen sollten.

---

## Schritt 2 – Selektoren, Vererbung und Kaskade

Mit CSS-Selektoren wählst du gezielt Elemente aus. Die Kaskade bestimmt, welche Regel gilt, wenn mehrere passen. Vererbung bedeutet, dass z.B. die Schriftfarbe von Eltern- auf Kindelemente übergeht.

Beispiel:
```css
.scoreboard-wrapper {
    background: var(--panel-bg);
    color: var(--text-color);
}
table#scoreboard th, table#scoreboard td {
    padding: 0.75rem 0.5rem;
}
```
- `.scoreboard-wrapper` wählt alle Elemente mit dieser Klasse.
- `table#scoreboard th, table#scoreboard td` wählt alle `<th>` und `<td>` in der Tabelle mit der ID `scoreboard`.

### Aufgabe 2:
- Schreibe einen eigenen Selektor, der z.B. die dritte Spalte der Tabelle einfärbt.
- Überlege, wie Vererbung und Kaskade in deinem Beispiel wirken.

---

## Schritt 3 – Grundlayout gestalten

Gestalte das Layout für `body` und `.scoreboard-wrapper`, sodass das Scoreboard zentriert und ansprechend aussieht. Nutze Variablen für Farben, Abstände und Schatten.

Beispiel:
```css
body {
    background: var(--main-bg);
    color: var(--text-color);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.scoreboard-wrapper {
    background: var(--panel-bg);
    border-radius: 20px;
    box-shadow: 0 4px 32px 0 #0008, 0 0 0 4px var(--accent);
    padding: 2.5rem 2.5rem 2rem 2.5rem;
    max-width: 480px;
    width: 100%;
    text-align: center;
    border: 2px solid var(--accent);
}
```

### Aufgabe 3:
- Passe das Layout an: Ändere z.B. die max-width, die Farben oder den Schatten.
- Erkläre, wie sich die Änderungen auf das Aussehen auswirken.
- Baue einen eigenen Hover-Effekt für die Tabelle ein.

---

## Schritt 4 – Media Queries und Responsive-Design

Mit Media Queries kannst du das Layout für verschiedene Bildschirmgrößen anpassen. Das ist die Grundlage für Responsive-Design.

Beispiel:
```css
@media (max-width: 600px) {
    .scoreboard-wrapper {
        padding: 1em 0.5em;
    }
    table, th, td {
        font-size: 0.95em;
    }
}
```
- `@media` leitet eine Media Query ein.
- `(max-width: 600px)` bedeutet: Die Regeln gelten nur, wenn das Fenster höchstens 600px breit ist.

### Aufgabe 4:
- Schreibe eine eigene Media Query für Tablets (z.B. 601–900px), die das Layout anpasst.
- Erkläre, wie die Bedingungen in der Media Query funktionieren.
- Probiere verschiedene Werte und beobachte die Auswirkungen beim Verkleinern des Browserfensters.

---

## Schritt 5 – Mini-Experimente & Verständnisfragen
- Was passiert, wenn du eine Variable im :root änderst?
- Wie kannst du das Layout noch flexibler machen?
- Wie würdest du das Scoreboard für sehr kleine Bildschirme (z.B. Smartphones) optimieren?
- Was passiert, wenn du mehrere Media Queries für verschiedene Bereiche schreibst?

---

## Komplette Lösung

<details>
<summary>Hier klicken, um die Lösung anzuzeigen</summary>

**scoreboard.css**
```css
:root {
    --main-bg: linear-gradient(120deg, #232526, #414345);
    --panel-bg: rgba(255, 255, 255, 0.95);
    --text-color: #232526;
    --accent: #1a8cff;
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
}
table#scoreboard tbody tr:nth-child(even) {
    background: #f7f7f733;
}
table#scoreboard tbody tr:hover {
    background: #e3e9f799;
}
@media (max-width: 600px) {
    table, th, td {
        font-size: 0.95em;
    }
    .scoreboard-wrapper {
        padding: 1em 0.5em;
    }
}
@media (min-width: 601px) and (max-width: 900px) {
    .scoreboard-wrapper {
        max-width: 90vw;
    }
}
```

</details> 
