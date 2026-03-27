import json
import os

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db_state.json")

def get_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)
    
def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4, default=str)
        
def get_last_sync(source: str):
    state=get_state()
    return state["sources"].get(source, {}).get("last_sync") or "1900-01-01 00:00:00"

def save_last_state(source: str, timestamp, count: int):
    state = get_state()
    state["sources"][source]["last_sync"] = str(timestamp)
    state["sources"][source]["sync_total"] += count
    save_state(state)
       