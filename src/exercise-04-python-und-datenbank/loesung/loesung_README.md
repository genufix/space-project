### Musterlösung – Mini-Übung 1

```python

def score_aktualisieren(name, neuer_score):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE players
            SET score = ?
            WHERE name = ?
        """, (neuer_score, name))

        conn.commit()
        print(f"✅ Score von {name} auf {neuer_score} aktualisiert!")

score_aktualisieren("AstroAlex", 99999)
```

### Musterlösung – Mini-Übung 2

```python
def spieler_loeschen(name):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM players WHERE name = ?", (name,))

        conn.commit()
        print(f"✅ {name} wurde aus der Rangliste entfernt!")

spieler_loeschen("GalaxyGreta")
alle_scores_anzeigen()
```