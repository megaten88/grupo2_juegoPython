import json
import random

categories = ['lenguaje','logica','ciencia','cultura','logica-matematica']

def fetch_data(category):
    """
    Funcion que devuelve todos los datos asociados a una categoria.
    INPUT: <type, str>: La categoria de juego.
    OUTPUT: <type, dict>: Datos asociados a la categoria (preguntas,respuestas,pistas,exp).
    """
    with open ('preguntas/' + category + '.json') as file:
        category_data = json.load(file)
        #category_data = dict(random.sample(category_data.items(),2)) #para dar aleatoriedad
        return(category_data)

#x = fetch_data('cultura')
#print(x)
#for key in list(x): #list(x) en lugar de x para evitar:RuntimeError: dictionary changed size during iteration
#    print(x.pop(key))

def player_input(question):
    """
    Funcion que le pide al usuario ingrese su respuesta a una pregunta.
    OUTPUT: <type, str>: Respuesta del jugador.
    INPUT: <type, str>: La pregunta que se le hace al jugador.
    """
    print(question)
    response = input().lower().strip()
    return(response)

def answer_check(question_data, protagonist):
    """
    Funcion que compara la respuesta ingresada por el jugador y la compara con la solución a la misma.
    INPUT: <type, dict>: Toda la data asociada a una preguntas
    OUTPUT: Por definirse
    """
    answer = question_data["respuesta"]
    response = player_input(question_data["problema"])
    if response == answer:
        print("Has acertado!")
        protagonist + question_data["exp"]
    else:
        print("No te rindas! Intenta de nuevo!")

class Question:
    def __init__(self,question, answer, hint, exp):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.exp = exp

#question1 = Question()
