from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DB_FILE = "incidents.db"

def get_all_incidents():
    conn = sqlite3.connect(DB_FILE)
    
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM incidents ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

@app.get("/")
def read_root():
    return {"message": "App is running"}

@app.get("/incidents")
def read_incidents():
    data = get_all_incidents()
    return data

@app.delete("/incidents")
def clear_incidents():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM incidents")
        conn.commit()
        return {"status": "succes", "message": "cleared"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        conn.close()
