# Übung 3 – Das Scoreboard-Table-Layout in HTML und CSS

In dieser Übung baust du die Grundstruktur für das Scoreboard: eine Tabelle, die später mit JavaScript gefüllt wird. Du lernst, wie man Tabellen in HTML anlegt und mit CSS gestaltet.

---

## Schritt 1 – Was ist eine Tabelle in HTML?

Tabellen sind ideal, um Daten wie Punktestände übersichtlich darzustellen. Sie bestehen aus:
- `<table>`: Das Tabellen-Element
- `<thead>`: Kopfzeile (Spaltenüberschriften)
- `<tbody>`: Tabellenkörper (Daten)
- `<tr>`: Tabellenzeile
- `<th>`: Tabellenkopf (fett, zentriert)
- `<td>`: Tabellendaten (normale Zelle)

Erinnerst du dich das wir über **Verschachtelung** gepsprochen haben? Tabellen sind ein tolles Beispiel für tags in tags.

### Aufgabe:
- Recherchiere: Was ist der Unterschied zwischen `<th>` und `<td>`?
- Was passiert, wenn du `<thead>` oder `<tbody>` weglässt?

---

## Schritt 2 – Baue die Tabelle in HTML

Füge in deine `scoreboard.html` innerhalb von `<div class="scoreboard-wrapper">` folgenden Code ein:

```html
<table id="scoreboard">
    <thead>
        <tr>
            <th>Rang</th>
            <th>Name</th>
            <th>Punkte</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Alice</td>
            <td>1200</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Bob</td>
            <td>950</td>
        </tr>
    </tbody>
</table>
```

**Erklärung:**
- Die Tabelle hat drei Spalten: Rang, Name, Punkte.
- Im `<tbody>` stehen zwei Beispiel-Spieler.

### Aufgabe:
- Schau dir den Code für die Tabelle genau an und mach dir klar was passiert.
- Mit welchen tags bekomme ich eine neue Zeile, wie eine neue Spalte?
- Füge eine weitere Zeile für einen dritten Spieler hinzu.

---

## Schritt 3 – Tabelle mit CSS gestalten

Füge in `scoreboard.css` folgende Regeln hinzu (oder erweitere die bestehenden Regeln):

```css
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
}
th, td {
    padding: 0.75em 0.5em;
    border-bottom: 1px solid #e0e0e0;
    text-align: center;
}
th {
    background: #232526;
    color: #fff;
    font-weight: 600;
}
tbody tr:nth-child(even) {
    background: #f7f7f7;
}
tbody tr:hover {
    background: #e3e9f7;
}
```

**Erklärung:**
- `border-collapse: collapse;` sorgt für saubere Kanten.
- `nth-child(even)` färbt jede zweite Zeile ein.
- `:hover` hebt die Zeile unter der Maus hervor.

### Aufgabe:
- Probiere andere Farben für die Kopfzeile oder Hover-Effekt aus.
- Wie kannst du die Spaltenbreite anpassen?

---

## Schritt 4 – Teste deine Seite

Speichere beide Dateien und öffne `scoreboard.html` im Browser. Die Tabelle sollte jetzt modern und übersichtlich aussehen.

---

