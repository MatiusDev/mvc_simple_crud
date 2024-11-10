from abc import ABC

class IDriver(ABC):
  def create_table(self):
    raise NotImplementedError("create_table method not implemented")
  
  def query(self):
    raise NotImplementedError("query method not implemented")
  
  def add(self, **kwargs):
    raise NotImplementedError("add_task method not implemented")
  
  def get_by_id(self, id):
    raise NotImplementedError("get_task method not implemented")
  
  def get_all(self):
    raise NotImplementedError("get_all_tasks method not implemented")
  
  def update(self, id, **kwargs):
    raise NotImplementedError("update_task method not implemented")
  
  def delete(self, id):
    raise NotImplementedError("delete_task method not implemented")