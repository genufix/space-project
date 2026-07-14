import sys, os
from datetime import date
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
"..","..")))
from database import get_db

def score_speichern(name, device_id, score, level):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO players (name, device_id, score, level, datum)
            VALUES (?, ?, ?, ?, ?)
        """, (name, device_id, score, level, str(date.today())))

        conn.commit()
        print(f"Score von {name} ({score} Punkte) gespeichert.")

score_speichern("AstroAlex", "badb7dc2-ad9a-4c8e-a96d-591f707bd5ed", 42000, 5)
score_speichern("GalaxyGreta", "3e3d1123-36f9-4237-a058-77b4f314475f", 38500, 3)
score_speichern("NebulaNiko", "9a1d0240-13ab-477c-a22a-3ac33d223fa7", 51200, 7)