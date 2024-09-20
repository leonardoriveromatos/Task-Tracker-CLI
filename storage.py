# storage.py
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Cargar tareas desde el archivo JSON."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Guardar tareas en el archivo JSON."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
