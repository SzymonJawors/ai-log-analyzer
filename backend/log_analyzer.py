import ollama
import time
import os
import sqlite3
from datetime import datetime


LOG_FILE="app_logs.log"
DB_FILE="incidents.db"

client = ollama.Client(host='http://host.docker.internal:11434')


def init_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS incidents (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp TEXT,
                       leveL TEXT,
                       content TEXT,
                       solution TEXT
                   ) 
                   """)
    conn.commit()
    conn.close()


def save_incident(level, content, solution):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute("""
                    INSERT INTO incidents (timestamp, level, content, solution) VALUES (?, ?, ?, ?)
                   """, (current_time, level, content, solution))
    conn.commit()
    conn.close()

def ask_ai_for_solution(error_msg):
    print(f"AI is analyzing...")
    try:
        response = client.chat(model='llama3.2:3b', messages=[
            {
                'role': 'system',
                'content': "You are a Senior DevOps Engineer and Security Expert. Analyze the provided log entry. Give a concise, 1-sentence technical solution in English. Be direct and professional."
            },
            {
                'role': 'user',
                'content': f'Error: {error_msg}',
            }
        ])
        return response['message']['content'].strip()
    except Exception as e:
        return f"Could not connect to AI: {e}"


def monitor_logs():
    print(f"Monitoring {LOG_FILE}")
    init_database()
    
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        
        try:
            while True:
                line = f.readline()
                
                if not line:
                    time.sleep(0.1)
                    continue
                
                log_line = line.strip()
                
                if "ERROR" in log_line or "WARNING" in log_line:
                    if "ERROR" in log_line:
                        level = "ERROR"
                    else:
                        level = "FAILED"
                    print(f"Problem detected")
                    print(f"Content: {log_line}")
                    solution = ask_ai_for_solution(log_line)
                    print(f"Solution: {solution}")
                    save_incident(level, log_line, solution)
                    print("Saved to database")
                    print("-"*40)
                else:
                    print(f"Log (OK): {log_line}")
            
        except KeyboardInterrupt:
            print("Stopped")
            
if __name__ == "__main__":
    if os.path.exists(LOG_FILE):
        monitor_logs()
    else:
        print(f"File {LOG_FILE} doesn't exists")