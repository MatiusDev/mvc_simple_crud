from views.task_view import TaskView

from models.adapters.db_adapter import DBAdapter
from models.db.task_model import TaskModel
from models.entities.task import Task

class TaskController:
  def __init__(self, db_adapter: DBAdapter):
    self.task_model = TaskModel(db_adapter)
  
  def add_task(self, task_title: str, task_description: str):
    task = Task(task_title, task_description)
    self.task_model.add_task(task.title, task.description)
    TaskView.show_new_task(task)
  
  def list_tasks(self):
    tasks = self.task_model.get_all_tasks()
    TaskView.show_all_tasks(tasks)
    
  def get_task(self, task_id: int):
    db_task = self.task_model.get_task(task_id)
    task = Task(db_task[1], db_task[2])
    TaskView.show_one_task(task)
  
  def update_task(self, task_id: int, task_title: str, task_description: str):
    task = Task(task_title, task_description)
    self.task_model.update_task(task_id, task_title, task_description)
    TaskView.show_updated_task(task)
  
  def delete_task(self, task_id: int):
    self.task_model.delete_task(task_id)
    TaskView.show_deleted_task(task_id)