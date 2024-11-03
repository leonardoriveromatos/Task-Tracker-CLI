from storage import load_tasks_from_json, save_tasks_to_json


# Add Task
def add_task(tasks, task_description):
    task_id = len(tasks) + 1  # Generar ID único
    new_task = {"id": task_id, "task": task_description, "state": "in progress"}  # Crear la nueva tarea
    tasks.append(new_task)  # Añadir la tarea a la lista
    return new_task, tasks  # Devolver la lista actualizada


def list_tasks():
    tasks = load_tasks_from_json()
    return tasks


def remove_task(tasks, task_id=None, task_name=None):
    if task_id:
        # Buscar la tarea por su ID
        task_to_remove = next((task for task in tasks if task["id"] == task_id), None)
        if task_to_remove:
            tasks.remove(task_to_remove)
            save_tasks_to_json(tasks)
            return True, task_id  # Devolver True si se eliminó por ID
        return False, task_id  # Devolver False si no se encontró la tarea por ID
    elif task_name:
        # Buscar la tarea por su nombre
        task_to_remove = next((task for task in tasks if task["task"] == task_name), None)
        if task_to_remove:
            tasks.remove(task_to_remove)
            save_tasks_to_json(tasks)
            return True, task_name  # Devolver True si se eliminó por nombre
        return False, task_name  # Devolver False si no se encontró la tarea por nombre

    return None, None  # Si no se proporcionó ni ID ni nombre


def remove_all(tasks):
    if tasks:
        tasks.clear()
        save_tasks_to_json(tasks)
        return True
    return False


def update_task(tasks, task_id=None, task_name=None, new_description=None, new_state=None):
    if task_id is not None:
        task_to_update = next((task for task in tasks if task["id"] == task_id), None)
    elif task_name is not None:
        task_to_update = next((task for task in tasks if task["task"] == task_name), None)
    else:
        return False, None
    if task_to_update:
        if new_description is not None:
            task_to_update["task"] = new_description
            return True, task_to_update
        elif new_state is not None:
            task_to_update["state"] = new_state
            return True, task_to_update
    else:
        return False, task_name if task_name else task_id


def list_tasks_done():
    tasks = load_tasks_from_json()
    tasks_list_done = []
    for task in tasks:
        if task["state"] == "Done":
            tasks_list_done.append(task)
    return tasks_list_done


def list_tasks_not_done():
    tasks = load_tasks_from_json()
    tasks_not_done = []
    if tasks:
        for task in tasks:
            if task["state"] == "Not done":
                tasks_not_done.append(task)
    return tasks_not_done


def list_tasks_in_progress():
    tasks = load_tasks_from_json()
    tasks_in_progress = []
    if tasks:
        for task in tasks:
            if task["state"] == "In progress":
                tasks_in_progress.append(task)
    return tasks_in_progress


def print_tasks(list_task: list):
    for task in list_task:
        print(f"ID: {task['id']}, Description: {task['task']}, State: {task['state']}")
