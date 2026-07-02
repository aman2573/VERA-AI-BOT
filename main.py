import os
import time
import threading
import subprocess
import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="VERA V2 Cloud Wrapper")

@app.get("/")
def home():
    return {"status": "online", "message": "VERA V2 cloud engine is running smoothly."}

import sys  # Add this import at the top of main.py if it isn't there!

@app.get("/run")
def run_bot_endpoint():
    try:
        # sys.executable gets the EXACT path to the running python.exe (inside your .venv)
        # This forces the subprocess to stay inside your virtual environment!
        script_path = os.path.abspath("VERA_AI_BOT.PY")
        result = subprocess.run(
            [sys.executable, script_path], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return {
            "status": "success", 
            "message": "VERA execution finished.",
            "output": result.stdout[:1000]  # Increased to 1000 chars so you see more logs
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error", 
            "message": f"Script failed with exit code {e.returncode}",
            "details": e.stderr
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- KEEP ALIVE BACKGROUND LOOP ---
def keep_alive():
    time.sleep(60)
    url = os.getenv("RENDER_EXTERNAL_URL")
    
    if not url:
        return

    print(f"[Keep-Alive] Thread active for: {url}")
    while True:
        try:
            requests.get(url, timeout=10)
        except Exception:
            pass
        time.sleep(720)

if __name__ == "__main__":
    if os.getenv("RENDER_EXTERNAL_URL"):
        threading.Thread(target=keep_alive, daemon=True).start()

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
