import sqlite3

from .I_db_driver import IDriver

class SQLiteDriver(IDriver):
  # Constructor para la conexión a la base de datos
  def __init__(self, db_name: str = "default_db"):
    self.__connection = sqlite3.connect(db_name)
    self.__query = ""
  
  @property
  def get_connection(self):
    return self.__connection
  
  def query(self, query):
    self.__query = query
  
  def create_table(self):
    with self.__connection:
      self.__connection.execute(self.__query)
      
  def add(self, **kwargs):
    values = tuple(kwargs.values()) 
    with self.__connection:
      self.__connection.execute(self.__query, values)
  
  def get_by_id(self, id):
    with self.__connection:
      return self.__connection.execute(self.__query, (id,)).fetchone()
  
  def get_all(self):
    with self.__connection:
      return self.__connection.execute(self.__query).fetchall()
    
  def update(self, **kwargs):
    values = tuple(kwargs.values())
    with self.__connection:
      self.__connection.execute(self.__query, values)
  
  def delete(self, id):
    with self.__connection:
      self.__connection.execute(self.__query, (id,))