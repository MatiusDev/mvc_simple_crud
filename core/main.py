from controllers.task_controller import TaskController
from models.adapters.db_adapter import DBAdapter

def main(db_adapter):
  while True:
    opt = input("""*** Bienvenido al RAT, menú principal ***\n
1. Listar tareas
2. Agregar tarea
3. Actualizar tarea
4. Eliminar tarea
0. Salir
\nIngrese su opción: """)
    task_controller = TaskController(db_adapter)
    match(opt):
      case "0":
        print("\nAdios!\n")
        break
      case "1":
        task_controller.list_tasks()
      case "2":
        print("\n***Agregar tarea***\n")
        task_title = input("Ingrese el titulo de la tarea: ")
        task_description = input("Ingrese la descripción de la tarea: ")
        task_controller.add_task(task_title, task_description)
      case "3":
        print("\n***Actualizar tarea***")
        task_id = int(input("Ingrese el id de la tarea: "))
        task_controller.get_task(task_id)
        print(f"\nPara actualizar esta tarea por favor ingrese lo siguiente:\n")
        task_title = input("Ingrese el titulo de la tarea: ")
        task_description = input("Ingrese la descripción de la tarea: ")
        task_controller.update_task(task_id, task_title, task_description)
      case "4":
        print("\n***Eliminar tarea***")
        task_id = int(input("Ingrese el id de la tarea: "))
        task_controller.delete_task(task_id)
      case _:
        print("\nError: Opción invalida, no se ha ejecutado ninguna operación.\n")
  
  db_adapter.close()
  

if __name__ == "__main__":
  db_adapter = DBAdapter("sqllite", "task_db")
  db_adapter.connect()
  db_adapter.create_table()
  main(db_adapter)