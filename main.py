import argparse
from tasks import add_task, list_tasks, remove_task, remove_all, update_task, list_tasks_done,list_tasks_not_done
from storage import load_tasks, save_tasks

# Crear el parser
parser = argparse.ArgumentParser(description="Task Tracker CLI")

# Definir comandos y argumentos
parser.add_argument("command", choices=["add", "update", "list", "list_done", "list_not_done","remove", "remove_all"], help="Comando a ejecutar")
parser.add_argument("--task", help="Tarea a añadir, actualizar o remover por su nombre", required=False)
parser.add_argument("--index", type=int, help="Índice de la tarea para actualizar o remover", required=False)
parser.add_argument("--new_description", help="Nueva descripción de la tarea", required=False)
parser.add_argument("--new_state", help="Nueva descripción del estado de la tarea", required=False)


# Parsear los argumentos
args = parser.parse_args()

# Cargar tareas desde el archivo
tasks = load_tasks()

if args.command == "add":
    if args.task:
        new_task, tasks = add_task(tasks, args.task)  # Añadir la tarea a la lista
        save_tasks(tasks)  # Guardar la lista en el archivo JSON
        print(f"Task added successfully, ID: '{new_task['id']}'")  # Confirmar al usuario
    else:
        print("Please use command --task for a new task")
elif args.command == "list":
    tasks = list_tasks()
    if tasks:
        print("Tasks List")
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['task']}, State: {task['state']}")
    else:
        print("There are no tasks in the list")
elif args.command == "remove":
    if args.index:
        succes, identifier = remove_task(tasks, task_id = int(args.index))
        if succes:
            print(f"Task with ID: {identifier} deleted")
        else:
            print(f"No tasks with ID: {identifier} found")
    elif args.task:
        succes, task_name = remove_task(tasks, task_name = args.task)
        if succes:
            print(f"Task with name: {task_name} deleted ")
        else:
            print(f"No tasks with name:{task_name} found")
    else:
        print("Provide an ID or name to delete the task")
elif args.command == "remove_all":
    succes = remove_all(tasks)
    if succes:
        print("Deleted tasks")
    else:
        print("The task list is already empty")
elif args.command == "update":
    if args.index:
        success, updated_task = update_task(tasks, task_id=int(args.index), new_description=args.new_description, new_state = args.new_state)
        if success:
            save_tasks(tasks)
            print("Updated successfully")
        else:
            print(f"No task found with ID: {args.index}")
    elif args.task:
        success, updated_task = update_task(tasks, task_name=args.task, new_description=args.new_description, new_state = args.new_state)
        if success:
            save_tasks(tasks)
            print("Updated successfully")
        else:
            print(f"No task found with name: {args.task}")
    else:
        print("Please provide either an ID or a name to update the task")
elif args.command == "list_done":
    tasks_done = list_tasks_done()
    if tasks_done:
        print("Tasks List Done")
        for task in tasks_done:
            print(f"ID: {task['id']}, Description: {task['task']}, State: {task['state']}")
    else:
        print("There are no tasks done in the list")
elif args.command == "list_not_done":
    tasks_not_ndone = list_tasks_not_done()
    if tasks_not_ndone:
        print("Tasks List Not Done")
        for task in tasks_not_ndone:
            print(f"ID: {task['id']}, Description: {task['task']}, State: {task['state']}")
    else:
        print("There are no tasks not done in the list")

    