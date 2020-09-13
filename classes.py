class Character:
   def __init__(self, name, level):
       self.name = name
       self.level = level
   def __str__(self):
    return "Nombre:{}\n Nivel:{}".format(self.name, self.level)