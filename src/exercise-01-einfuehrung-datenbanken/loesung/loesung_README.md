### Musterlösung – Mini-Übung 1

**Tabelle: `spieler`**

| id | name        | erstellt_am |
|----|-------------|-------------|
| 1  | AstroAlex   | 2024-06-10  |
| 2  | GalaxyGreta | 2024-06-10  |

**Tabelle: `scores`**

| id | spieler_id | score | level | erreicht_am |
|----|------------|-------|-------|-------------|
| 1  | 1          | 42000 | 5     | 2024-06-10  |
| 2  | 1          | 55000 | 7     | 2024-06-11  |
| 3  | 2          | 38500 | 3     | 2024-06-10  |

Die `spieler_id` in der `scores`-Tabelle verweist auf den Spieler in der `spieler`-Tabelle.
So weiß man immer, welcher Spieler welchen Score hat – auch wenn zwei Spieler denselben Namen hätten.

---

### Musterlösung – Mini-Übung 2

Probleme mit der Tabelle:
1. Die Spalte `name` kommt **zweimal** vor – das ist ungültig
2. Es gibt keine `id` – man kann die beiden Einträge von „Alex" nicht unterscheiden

Richtig wäre:

| id | name | score |
|----|-------------|-------|
| 1  | Alex        | 1000  |
| 2  | Alex        | 2000  |
