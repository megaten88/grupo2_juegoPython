class Character:
   def __init__(self, name, level):
       self.name = name
       self.level = level
   def __str__(self):
    return "Nombre:{}\n Nivel:{}".format(self.name, self.level)


class Protagonist(Character):
    def __init__(self, name, level, exp=1, nextLevel=80,tryNumber=3):
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
    pass

class Planet:
    def __init__(self, name, category, villain):
        self.name = name
        self.category = category
        self.villain = villain
    def __str__(self):
        return "Nombre:{}\n Categoria:{}".format(self.name, self.category)

categorias = ["Cultura General", "Música", "Lenguajes"] 

def lectura():
    nueva_pregunta = Question(0,"Como estás?", 20)
    pass

class Question:
    def __init__(self, numCategory, question, exp):
        self.category = numCategory
        self.question = question
        self.exp = exp
    

question1 = Question(0,"¿Donde quedá Japón?",20)

preguntas = [question1]


personaje = Protagonist("Mayra",1,1)
print(personaje)
print()

personaje + question1.exp

print(personaje)

