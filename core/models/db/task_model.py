from models.adapters.db_adapter import DBAdapter

class TaskModel:
  # Constructor para la conexión a la base de datos
  def __init__(self, db_adapter):
    self.adapter = db_adapter
  
  def create_table(self):
    self.adapter.create_table()
      
  def add_task(self, title, description):
    self.adapter.add_task(title, description)
  
  def get_task(self, id):
    return self.adapter.get_task(id)
  
  def get_all_tasks(self):
    return self.adapter.get_all_tasks()
    
  def update_task(self, id, title, description):
    self.adapter.update_task(id, title, description)
    
  def delete_task(self, id):
    self.adapter.delete_task(id)