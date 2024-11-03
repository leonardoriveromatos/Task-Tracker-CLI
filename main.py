import argparse

from storage import load_tasks_from_json, save_tasks_to_json
from tasks import add_task, list_tasks, remove_task, remove_all, update_task, list_tasks_done, list_tasks_not_done, \
    list_tasks_in_progress, print_tasks


def create_commands():
    # Crear el parser
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    # Definir comandos y argumentos
    parser.add_argument("command",
                        choices=["add", "update", "list", "list_done", "list_not_done", "list_in_progress", "remove",
                                 "remove_all"], help="Comando a ejecutar")
    parser.add_argument("--task", help="Tarea a añadir, actualizar o remover por su nombre", required=False)
    parser.add_argument("--index", type=int, help="Índice de la tarea para actualizar o remover", required=False)
    parser.add_argument("--new_description", help="Nueva descripción de la tarea", required=False)
    parser.add_argument("--new_state", help="Nueva descripción del estado de la tarea", required=False)
    return parser


def main():
    parser = create_commands()
    # Parsear los argumentos
    args = parser.parse_args()
    # Cargar tareas desde el archivo
    tasks = load_tasks_from_json()
    if args.command == "add":
        add_command(args, tasks)
    elif args.command == "list":
        list_command()
    elif args.command == "remove":
        remove_command(args, tasks)
    elif args.command == "remove_all":
        remove_all_command(tasks)
    elif args.command == "update":
        update_command(args, tasks)
    elif args.command == "list_done":
        list_done_command()
    elif args.command == "list_not_done":
        list_not_done_command()
    elif args.command == "list_in_progress":
        list_in_progress_command()


def list_in_progress_command():
    tasks_in_progress = list_tasks_in_progress()
    if tasks_in_progress:
        print("Tasks List In Progress")
        print_tasks(tasks_in_progress)
    else:
        print("There are no tasks in progress in the list")


def list_not_done_command():
    tasks_not_done = list_tasks_not_done()
    if tasks_not_done:
        print("Tasks List Not Done")
        print_tasks(tasks_not_done)
    else:
        print("There are no tasks not done in the list")


def list_done_command():
    tasks_done = list_tasks_done()
    if tasks_done:
        print("Tasks List Done")
        print_tasks(tasks_done)
    else:
        print("There are no tasks done in the list")


def update_command(args, tasks):
    if args.index:
        success, updated_task = update_task(tasks, task_id=int(args.index), new_description=args.new_description,
                                            new_state=args.new_state)
        if success:
            save_tasks_to_json(tasks)
            print("Updated successfully")
        else:
            print(f"No task found with ID: {args.index}")
    elif args.task:
        success, updated_task = update_task(tasks, task_name=args.task, new_description=args.new_description,
                                            new_state=args.new_state)
        if success:
            save_tasks_to_json(tasks)
            print("Updated successfully")
        else:
            print(f"No task found with name: {args.task}")
    else:
        print("Please provide either an ID or a name to update the task")


def remove_all_command(tasks):
    success = remove_all(tasks)
    if success:
        print("Deleted tasks")
    else:
        print("The task list is already empty")


def remove_command(args, tasks):
    if args.index:
        success, identifier = remove_task(tasks, task_id=int(args.index))
        if success:
            print(f"Task with ID: {identifier} deleted")
        else:
            print(f"No tasks with ID: {identifier} found")
    elif args.task:
        success, task_name = remove_task(tasks, task_name=args.task)
        if success:
            print(f"Task with name: {task_name} deleted ")
        else:
            print(f"No tasks with name:{task_name} found")
    else:
        print("Provide an ID or name to delete the task")


def list_command():
    tasks = list_tasks()
    if tasks:
        print("Tasks List")
        print_tasks(tasks)
    else:
        print("There are no tasks in the list")


def add_command(args, tasks):
    if args.task:
        new_task, tasks = add_task(tasks, args.task)  # Añadir la tarea a la lista
        save_tasks_to_json(tasks)  # Guardar la lista en el archivo JSON
        print(f"Task added successfully, ID: '{new_task['id']}'")  # Confirmar al usuario
    else:
        print("Please use command --task for a new task")


if __name__ == '__main__':
    main()