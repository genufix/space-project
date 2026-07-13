# Übung 1 – HTML-Grundstruktur und Grundlagen für das Scoreboard

In dieser Übung legst du die Basis für dein Scoreboard-Projekt. Du lernst die wichtigsten HTML-Grundlagen und erstellst eine HTML-Datei mit allen wichtigen Elementen, die später für das echte Projekt gebraucht werden.

---

## Schritt 1 – Was ist HTML überhaupt?

HTML steht für **HyperText Markup Language**. Es ist die Sprache, mit der Webseiten aufgebaut werden. HTML beschreibt die **Struktur** einer Seite: Überschriften, Absätze, Listen, Bilder, Container usw.

- **HTML besteht aus sogenannten "Tags"**
`<h1>` ist eine Überschrift, `<p>` ein paragraph also neuer Absatz und ein `<div>` ist ein Container, also ein Feld das andere HTML Daten enthält. Jedes Tag hat eine bestimmte Bedeutung. 
Wenn du mal einen bestimmten Tag nachschauen willst schaue unter folgenden Links oder google:
	- [w3schools](https://www.w3schools.com/tags/default.asp)
	- [mdn docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)
- **Tags werden meist paarweise verwendet**:
Ein öffnendes Tag `<div>` und ein schließendes Tag `</div>`. Zwischen beide Tags kommt der Inhalt, also z.B. so: `<h1>Meine Überschrift</h1>`
- **Attribute** (z.B. `lang="de"` oder `class="scoreboard-wrapper"`) geben zusätzliche Informationen zu einem Tag. Sie werden in den Tag geschrieben, z.B. `<h1 id="titel">Meine Überschrift</h1>`  Dazu später mehr.
- **Kommentare** in HTML schreibt man so: `<!-- Das ist ein Kommentar -->`.
Sie werden im Browser nicht angezeigt. Das kann nützlich sein wenn du dir den Code strukturieren möchtest.

### Aufgabe:
- Erstelle im "src"-Ordner einen Unterordner namens "projekt". Dort kommt dann dein Projekt hinein. Bitte schreibe allen Code in Dateien in diesen Ordner, damit er an einer einheitlichen Stelle liegt. Bei manchen Übungen sind Dateien vorhanden, die du als Hilfestellung verwenden kannst.
- Erstelle eine Datei namens "scoreboard.html". Dort kommt dein Quellcode hinein. 
- Schreibe ein Beispiel für ein HTML-Tag mit Attribut und Kommentar in eine neue Datei und öffne sie im Browser. Was passiert?
- Recherchiere: Was ist der Unterschied zwischen `<h1>` und `<p>`? Probiere gerne verschiedene tags aus und schaue wie sie dargestellt werden.

---

## Schritt 2 – Die Grundstruktur einer HTML-Seite

Jede HTML-Seite hat ein festes Grundgerüst. Das sieht so aus:

```html
<!DOCTYPE html> <!-- Sagt dem Browser, dass es sich um HTML5 handelt. -->
<html lang="de"> <!-- Start des HTML-Dokuments, Sprache ist Deutsch. -->
<head>
    <meta charset="UTF-8"> <!-- Zeichencodierung, damit Umlaute funktionieren. -->
    <title>Space Scoreboard</title> <!-- Der Titel, der im Browser-Tab angezeigt wird. -->
</head>
<body>
    <!-- Hier kommt später unser Scoreboard hin: -->
    <div class="scoreboard-wrapper">
        <!-- Noch leer, wird in den nächsten Übungen gefüllt! -->
    </div>
</body>
</html>
```

**Erklärung:**
- `<!DOCTYPE html>`: Sagt dem Browser, dass es sich um HTML5 handelt.
- `<html lang="de">`: Start des HTML-Dokuments, Sprache ist Deutsch. Unser gesamter Code befindet sich in einem `<html></html>` tag.
- `<head>`: Enthält "Meta-Informationen" (z.B. Zeichencodierung, Titel, später auch CSS und JS).
- `<meta charset="UTF-8">`: Zeichencodierung, damit Umlaute und Sonderzeichen funktionieren.
- `<title>`: Der Text, der im Browser-Tab angezeigt wird.
- `<body>`: Hier steht alles, was auf der Seite sichtbar ist.
- `<div class="scoreboard-wrapper">`: Ein "Container" für unser Scoreboard. Mit `class` kann man das Element später mit CSS gestalten.

Super reduziert kann man die html-Struktur auch so darstellen:

```html
<!DOCTYPE html>
<html>
	<head> </head>
	<body> </body>
</html>
```

Dabei ist es wichtig zu verstehen, dass in html tags oft **verschachtelt** werden, also tags werden in tags platziert. Das ist wichtig für die Struktur einer html-Seite,
damit wir bestimmen können wo ein Element erscheint. Tags die sich in einem anderen Tag befinden werden zur besseren Lesbarkeit gerne mit einem Tabulator (neben der q-Taste)
eingerückt. Im folgenden Beispiel wird dem `<header>` tag ein `<h1>` tag zugefügt.

```html
<!DOCTYPE html>
<html>
	<head> </head>
	<body> 
		<header>
			<h1>Meine Überschrift</h1>
		</header>
	</body>
</html>
```

### Aufgabe:
- Ändere den `<title>` auf einen eigenen Namen, z.B. „Mein Space Scoreboard“.
- Füge einen eigenen Kommentar im `<body>` ein, was du später anzeigen möchtest.
- Füge ein weiteres Tag deiner Wahl (z.B. `<h1>`, `<p>`, `<ul>`) in den Body ein und beschreibe, was es macht.
- Wenn du nicht weißt, wie man ein `<div>` anlegt, google: „html div element“.

---

## Schritt 3 – Wie zeigt der Browser HTML an?

- Der Browser liest die HTML-Datei und "baut" daraus die Webseite.
- Kommentare werden **nicht** angezeigt.
- Der `<title>` erscheint im Tab, alles im `<body>` auf der Seite.
- Wenn du einen Fehler im HTML machst (z.B. einen Tag nicht schließt), kann die Seite komisch aussehen.

### Aufgabe:
- Probiere aus, was passiert, wenn du vergisst einen Tag zu schließen?
- Recherchiere: Wie kann man HTML online "validieren" (auf Fehler prüfen)?

---

## Schritt 4 – Teste deine Seite

Speichere die Datei und öffne sie im Browser mit `Datei/öffnen DATEINAME` oder doppelklck auf die .html Datei. Du solltest einen leeren Bereich sehen (später kommt dort das Scoreboard hin) und im Tab deinen gewählten Titel.

---

## Schritt 5 – Bonus: HTML weiter entdecken

- Probiere weitere Tags aus: `<h2>`, `<ul>`, `<li>`, `<img>`, `<a>` ...
- Schau dir im Browser mit Rechtsklick → "Element untersuchen" den HTML-Code an.
- Lies auf [MDN Web Docs](https://developer.mozilla.org/de/docs/Web/HTML) mehr über HTML.

## Schritt 6 – Erstelle dein Projektverzeichnis

Wenn du das noch nicht getan hast: Erstelle einen Ordner, in den du deine Dateien schreiben wirst. Diesen Ordner kannst du dann für die Erstellung des Projektes verwenden.
---
