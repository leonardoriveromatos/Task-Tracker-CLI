# Task Tracker CLI

## Descripción
***Task Tracker es un proyecto utilizado para rastrear y gestionar tus tareas. Con esta herramienta podrás crear, listar y eliminar tareas directamente desde la línea de comandos. Te permite realizar un seguimiento de lo que necesitas hacer, lo que has hecho y en lo que estás trabajando actualmente. Este proyecto te ayudará a practicar tus habilidades de programación, incluyendo el trabajo con el sistema de archivos, manejo de entradas de usuario y la construcción de una aplicación CLI sencilla.***

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/leonardoriveromatos/Task-Tracker-CLI.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd task-tracker-cli
   ```

3. Asegúrate de tener Python instalado y ejecuta el siguiente script para ver el menú de ayuda
   ```bash
   python main.py -h
   ```

## Comandos disponibles

### 1. `add`
Agrega una nueva tarea a la lista de tareas.


**Ejemplo**:
```bash
python main.py add --task "Estudiar Python"
```

**Salida esperada**:
```bash
Task added successfully, ID: '1'
```

### 2. `list`
Muestra todas las tareas almacenadas, incluyendo su índice, nombre y estado.

**Ejemplo**:
```bash
python main.py list
```

**Salida esperada**:
```bash
Tasks List
ID: 1, Description: Estudiar Python, State: in progress
```
### 3. `list_done`
Muestra todas las tareas que esten realizadas almacenadas, incluyendo su índice, nombre y estado.

**Ejemplo**:
```bash
python main.py list_done
```

**Salida esperada**:
```bash
Tasks List Done
ID: 1, Description: Estudiar Python, State: Done
```

### 4. `list_not_done`
Muestra todas las tareas que no esten realizadas almacenadas, incluyendo su índice, nombre y estado.

**Ejemplo**:
```bash
python main.py list_not_done
```

**Salida esperada**:
```bash
Tasks List Not Done
ID: 1, Description: Estudiar Python, State: Not done
```

### 5. `remove`
Elimina una tarea de la lista por su nombre o índice.

**Ejemplo**:
```bash
python main.py remove --index 1
```

**Salida esperada** (si se elimina con éxito):
```bash
Task with ID: 1 deleted
```
**Salida esperada** (si no se encuentra la tarea):
```bash
No tasks with ID: 1 found
```

**Ejemplo** (eliminando por nombre):
```bash
python main.py remove --task "Estudiar Python"
```

**Salida esperada** (si se elimina con éxito):
```bash
Task with name: Estudiar Python deleted
```
**Salida esperada** (si no se encuentra la tarea):
```bash
No tasks with name: Estudiar Python found
```

### 6. `remove_all`
Elimina todas las tareas de la lista.


**Ejemplo**:
```bash
python main.py remove_all
```

**Salida esperada** (si se eliminan las tareas):
```bash
Deleted tasks
```
**Salida esperada** (si la lista ya está vacía):
```bash
The task list is already empty
```

### 7. `update`
Actualiza la descripción o el estado de una tarea de la lista mediante su id o nombre.

**Ejemplo**: ***Actualizando el estado de la tarea mediante el id***
```bash
python main.py --index 1 update --new_state "Done"
```
**Ejemplo**: ***Actualizando el estado de la tarea mediante la descripcion***
```bash
python main.py --task "Hacer la tarea" update --new_state "Done"
```
**Ejemplo**: ***Actualizando la nueva descripcion de la tarea mediante la descripcion actual***
```bash
python main.py --task "Hacer la tarea" update --new_description "Hacer la tarea y estudiar python"
```
**Ejemplo**: ***Actualizando la nueva descripcion mediante el id***
```bash
python main.py --index 1 update --new_description "Hacer la tarea y estudiar python"
```
**Salida esperada** (si se actualiza con éxito):
```bash
Updated successfully
```
**Salida esperada** (si no se encuentra la tarea por su ID):
```bash
No tasks with ID: 1 found
```
**Salida esperada** (si no se encuentra la tarea por su descripcion):
```bash
No task found with name: Hacer la tarea
```

## Contribuciones
***Si quieres contribuir a este proyecto, siéntete libre de hacer un fork y crear un pull request con tus mejoras.***