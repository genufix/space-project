import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from database import get_db

with get_db() as conn:
    cursor = conn.cursor()
    cursor.execute("Select * FROM players")

    ergebnisse = cursor.fetchall()
    print(ergebnisse)