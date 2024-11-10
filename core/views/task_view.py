from models.entities.task import Task

class TaskView:
  def show_all_tasks(tasks: dict):
    print("\n***Listado de tareas***\n")
    for id, title, description in tasks:
      print(f"Tarea [{id}]:\n\tTitulo: {title}\n\tDescripción: {description}")
    print("")
  
  def show_one_task(task: Task):
    if task == None:
      print("Error, no se ha encontrado la tarea")
    
    print(f"Tarea:\n\tTitulo: {task.title}\n\tDescripción: {task.description}")
  
  def show_new_task(task: Task):
    print(f"Se ha agregado la tarea: {task}")
    
  def show_updated_task(task: Task):
    print(f"Se ha actualizado la tarea: {task}")
    
  def show_deleted_task(task: Task):
    print(f"Se ha eliminado la tarea: {task}")