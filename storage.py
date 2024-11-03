import json
import os

TASKS_FILE = "tasks.json"

def load_tasks_from_json():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks_to_json(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
