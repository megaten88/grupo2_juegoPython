from pregunta import Question

class Character:
   def __init__(self, name, level):
       self.name = name
       self.level = level
   def __str__(self):
    return "Nombre:{}\n Nivel:{}".format(self.name, self.level)


class Protagonist(Character):
    def __init__(self, name, level, exp=1, nextLevel=20,tryNumber=3):
        super().__init__(name,level)
        self.exp = exp
        self.nextLevel = nextLevel
        self.tryNumber = tryNumber
    def __str__(self):
        return f"Nombre:{self.name}\nNivel:{self.level}\nEXP:{self.exp}\nNext Level:{self.nextLevel}"
    def __add__(self,exp):
        self.exp += exp
        if(self.exp >= self.nextLevel):
            self.level+=1
            print("Subiste un nivel!\n")
            self.nextLevel+= self.nextLevel*2


class Villain(Character):
    def __init__(self, name, level,planet):
        super().__init__(name,level)
        self.planet = planet
    def __str__(self):
        return f"Soy {self.name},guardian del planeta {self.planet}"
    
    
class Planet:
    def __init__(self, name, category, villain):
        self.name = name
        self.category = category
        self.villain = Villain(villain,20,category)
    def __str__(self):
        return "Planeta:{}\n Categoría:{} \n Guardian: {}".format(self.name, self.category,self.villain)

