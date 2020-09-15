import json
import random

# categories = ['lenguaje','logica','ciencia','cultura','logica-matematica']

class Question:
    def __init__(self,question, answer, hint, exp):
        self.question = question
        self.answer = answer
        self.hint = hint
        self.exp = exp

    def __str__(self):
        return f"{self.question}"

def fetch_data(category):
    """
    Funcion que devuelve todos los datos asociados a una categoria.
    INPUT: <type, str>: La categoria de juego.
    OUTPUT: <type, dict>: Datos asociados a la categoria (preguntas,respuestas,pistas,exp).
    """
    with open ('archivos_json/' + category + '.json') as file:
        category_data = json.load(file)
        category_data = dict(random.sample(category_data.items(),2)) #para dar aleatoriedad
        return(category_data)

# x = fetch_data('cultura')
# print(type(x))
# print(x)
#for key in list(x): #list(x) en lugar de x para evitar:RuntimeError: dictionary changed size during iteration
#    print(x.pop(key))
def createQuestions(category):
    questions = []
    category_data = fetch_data(category)
    for key in category_data.keys():
        question = category_data[key]['pregunta']
        answer  = category_data[key]['respuesta']
        hint  = category_data[key]['pista']
        exp = category_data[key]['exp']
        newQuestion = Question(question,answer,hint,exp)
        questions.append(newQuestion)
    return questions

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
    answer = question_data.answer
    response = player_input(question_data)
    if response == answer:
        print("Has acertado!")
        protagonist + question_data.exp
        return True

    else:
        print("No te rindas! Intenta de nuevo!")
        return None



