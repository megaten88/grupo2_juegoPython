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

personaje = Protagonist("Mayra",1,1)
print(personaje)
print()

personaje + 80
print(personaje)