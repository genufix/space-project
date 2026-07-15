import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from database import get_db

def alle_scores_anzeigen():
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM players ORDER BY score DESC")
        eintraege = cursor.fetchall()

        print("\n🏆 SPACE INVADERS HIGHSCORES 🏆")
        print("-" * 45)

        for platz, eintrag in enumerate(eintraege, start=1):
            id, name, device_id, score, level, datum = eintrag
            print(f"  {platz}. {name:<15} {score:>8} Punkte  (Level {level})")

        print("-" * 45)

alle_scores_anzeigen()


def scores_aktualisieren(name,neuer_score):
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE players
            SET score = ? 
            WHERE name = ?
        """,   (neuer_score,name))
        conn.commit()

scores_aktualisieren("AstroAlex",99999)

def spieler_loeschen(name):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM players WHERE name = ?",(name,))
        conn.commit()

spieler_loeschen("GalaxyGreta")
spieler_loeschen("AstroAlex")
spieler_loeschen("NebulaNiko")
alle_scores_anzeigen()


