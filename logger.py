import json
from datetime import datetime

LOG_FILE = "focus_log.json"

def log_event(site_or_window, action):
    event = {
        "timestamp": datetime.now().isoformat(),
        "site_or_window": site_or_window,
        "action": action
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception as e:
        print("Error logging event:", e)