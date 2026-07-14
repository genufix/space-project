import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from database import get_db

def alle_scores_anzeigen():
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("Select * FROM players ORDER BY score DESC")
        eintraege = cursor.fetchall()

        print("\n SPACE INVADERS HIGHSCORE")
        print("-" * 45)
        
        for platz, eintrag in enumerate(eintraege, start=1):
            id, name, device_id, score, level, datum = eintrag
            print(f"  {platz}. {name:<15} {score:>8} Punkte  (Level {level})")
            
        print("-" * 45)

alle_scores_anzeigen()