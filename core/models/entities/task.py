class Task:
  def __init__(self, title: str, description: str):
    self.title = title
    self.description = description
    
  def __str__(self) -> str:
    return f"\n\tTitulo: {self.title}\n\tDescripción: {self.description}"