from .drivers.sqlite_db_driver import SQLiteDriver

class DBAdapter():
  def __init__(self, db_url: str, db_name) -> None:
    self.db_url = db_url
    self.db_name = db_name
    self.driver = None
   
  def connect(self):
    if (self.db_url == "sqllite"):
      self.driver = SQLiteDriver(self.db_name)
      print("Conectado a la base de datos SQLite")
    else:
      raise ValueError("La base de datos no es soportada")
    
  def create_table(self):
    self.driver.query("""
      CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
      );
    """)
    self.driver.create_table()
    
  def add_task(self, title, description):
    self.driver.query("INSERT INTO tasks (title, description) VALUES (?, ?);")
    self.driver.add(title=title, description=description)
    
  def get_task(self, id):
    self.driver.query("SELECT * FROM tasks WHERE id = ?;")
    return self.driver.get_by_id(id)
    
  def get_all_tasks(self):
    self.driver.query("SELECT * FROM tasks;")
    return self.driver.get_all()
  
  def update_task(self, id, title, description):
    self.driver.query("UPDATE tasks SET title = ?, description = ? WHERE id = ?;")
    self.driver.update(title=title, description=description, id=id)
  
  def delete_task(self, id):
    self.driver.query("DELETE FROM tasks WHERE id = ?;")
    self.driver.delete(id)
  
  def close(self):
    self.driver.get_connection.close()
    print("Desconectado de la base de datos")