import sqlite3
import os
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from database import get_db

app = FastAPI()


origins = ["http://localhost", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def calculate_score(asteroids_destroyed: int, time_lived: float) -> int:
    if asteroids_destroyed < 0 or time_lived < 0:
        raise ValueError("Negative Werte sind nicht erlaubt")
    return asteroids_destroyed * 100 + int(time_lived)

@app.get("/")
def start():
    return {"nachricht": "Hallo Welt, mein Backend läuft!"}


@app.get("/hallo/{name}")
def hallo(name: str):
    return {"nachricht": f"Hallo, {name}!"}

@app.get("/spieler")
def get_alle_spieler():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, device_id, score, level, datum FROM players")
        zeilen = cursor.fetchall()
        
    return [
        { 
            "id": z [0],
          "name": z [1],
          "device_id": z [2],
          "score": z [3], 
          "level": z [4],
          "datum": z [5],         
        }
        
         for z in zeilen
    ]

@app.get("/spieler{spieler_id}")
def get_ein_spieler(spieler_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, device_id, score, level, datum FROM players WHERE id = ?",
            (spieler_id,))
        zeile = cursor.fetchone()

    if zeile is None:
        raise HTTPException(status_code=404, detail="Spieler nicht gefunden")

    return {
        "id": zeile[0],
        "name": zeile[1],
        "device_id": zeile[2],
        "score": zeile[3],
        "level": zeile[4],
        "datum": zeile[5],
    }




@app.post("/spieler", status_code=201)
def post_spieler(device_id: str ,name: str):
    now = datetime.now(timezone.utc).isoformat()

    with get_db() as conn:
        cur = conn.cursor()

        cur.execute(
            "SELECT id FROM players WHERE name = ? AND device_id = ?",
            (name, device_id),
        )
        if cur.fetchone() is not None:
            raise HTTPException(status_code=409, detail="Spieler existiert bereits")

        score = 0
        cur.execute(
            "INSERT INTO players (name, device_id, score, level, datum) VALUES (?, ?, ?, ?, ?)",
            (name, device_id, score, None, now),
        )
        player_id = cur.lastrowid
        conn.commit()

    return {
        "id": player_id,
        "device_id": device_id,
        "name": name,
        "score": score,
        "level": None,
        "datum": now,
    }
@app.put("/spieler/{spieler_id}/scores")
def put_scores(spieler_id:int ,asteroids_destroyed: int,time_lived: float):
    try:
        score = calculate_score(asteroids_destroyed, time_lived)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    now = datetime.now(timezone.utc).isoformat()
    
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT id FROM players WHERE id = ?", (spieler_id,))
        if cursor.fetchone() is None:
            raise HTTPException(status_code=404, detail="Spieler nicht gefunden")
    
    
        cursor.execute("""
            UPDATE players
            SET score = ?
            datum = ?
            WHERE id = ?
        """,   (score,now,spieler_id))
        conn.commit()
    
    
    cursor.execute("SELECT id, name, device_id, score, level, datum FROM players WHERE id = ?",
            (spieler_id,),
        )
    zeile = cursor.fetchone()

    return {
        "id": zeile[0],
        "name": zeile[1],
        "device_id": zeile[2],
        "score": zeile[3],
        "level": zeile[4],
        "datum": zeile[5],
    }

@app.get("/scores")
def leaderboard(limit: int = 15):
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, name, device_id, score, level, datum FROM players ORDER BY score DESC LIMIT ?",
            (limit,),
        )
        rows = cur.fetchall()

    return [
        {
            "id": r[0],
            "name": r[1],
            "device_id": r[2],
            "score": r[3],
            "level": r[4],
            "datum": r[5],
        }
        for r in rows
    ]