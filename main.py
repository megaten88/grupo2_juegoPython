from  pregunta import *
from  classes import *
import textwrap

"""
    Esta parte es donde definimos lo que usaremos en el juego.
"""

def printInit():
    print (textwrap.dedent("""\
    #######################################
             Space Trivia
   ,-"     "-.
            / o       o \j\
           /   \     /   \\
          /     )-"-(     \\
         /     ( 6 6 )     \\
        /       \ " /       \\
       /         )=(         \\
      /   o   .--"-"--.   o   \\
     /    I  /  -   -  \  I    \\
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| hjw
         `==.___________.==' `97


          J - Jugar
          A - Ayuda
          C - Créditos
          S - Salir
    #######################################
    """))
    print()

def printCredits():
    print(textwrap.dedent("""\
    #######################################
            	 Copyright
        
        Pamela Salazar
        Allan Alonzo
        Mayra Salazar
        Bessy Padilla
    	Fernanda Medina

    #######################################
        """))
    print()

def printHelp():
    print(textwrap.dedent("""\
    #######################################
        Prepárate para una gran aventura.
        Este juego se trata de responder preguntas tipo trivia, entre más sepas, más fácil irás avanzando.

    #######################################
        """))


def createPlanet(name, category, villainName):
    planet = Planet(name, category, villainName)
    villain = planet.villain
    return (planet,villain)


def game():
    print(textwrap.dedent("""\
    … Si estas leyendo este mensaje debes ser el terrícola que he buscado durante tanto tiempo.
    Dime, ¿Cuál es tu nombre?\n
        """))

    name = input("Ingresa el nombre del personaje: ")
    protagonist = Protagonist(name,1,1)

    print(textwrap.dedent(f"""\
        {protagonist.name} ¡perfecto! Mucho gusto, mi nombre es Core y nadie conoce este lado del universo mejor que yo, o al menos eso es lo que dicen jeje. 
        - Core: Ohh amigo, te ves algo perdido… 
        - Core: Hmmmmmmmmm,, ¿que te parece si te unes a mi mas reciente y emocionante misión? Te explicare mas en el camino, ¡vamos!
        .
        .
        .
            """))
    playerChoice = input("**¿Viajar junto a Core?\n [Sí(S)/No(N)]: ").lower().strip()
    if(playerChoice[0]=="n"):
        print("Core: Está bien, entiendo, espero verte pronto amigo.")
        return
    print(textwrap.dedent(f"""\
        - Core: Gracias por acompañarme en esta aventura, te explico. 
        - Core: Nuestra misión es recolectar los 5 objetos especiales cada uno se encuentra resguardado por un guardián de planeta. Y para llegar a el debemos romper los sellos que los protegen ¿de que manera? 
        - Core: Pues respondiendo de forma correcta una serie de preguntas que nos harán debemos tener mucho cuidado pues si fallamos mas de 3 veces seremos descubiertos y exiliados del planeta. 
        - Core: Yo confió plenamente en tus habilidades, pero si te sientes en demasiados problemas puedo ayudarte recuerda que somos compañeros, ante todo.
        - Core: Cada planeta nos dará por su nombre la pista de que tipo de trivia o acertijo podremos encontrar en el, así que adelante y comencemos con el planeta del Lenguaje…
            """))

 # Aquí empieza la dinámica para todos los planetas 
    planet,villain = createPlanet("Planeta Lenguaje", "lenguaje", "Sir.Lovial")
    print(textwrap.dedent(f"""\
        *************LLEGANDO A {planet.name}
        - {villain.name}: Un terrícola y un bandido en el planeta del lenguaje, desde que entraron sabia que venían a por mi objeto. 
        - {villain.name}: al haber derrocado nuestros sellos han demostrado astucia, y valor. 
        - {villain.name}: Ahora, enfrentad con dignidad, y si sois merecedores lleváis el objeto con vosotros. 
            """))
    createQuestions('lenguaje') 
    print(questions)

    for question in questions:
        correct = None
        tries=0
        while(correct is None and tries<= protagonist.tryNumber):
            correct = answer_check(question,protagonist)
            if(correct is None ):
                tries+=1
            if(tries == protagonist.tryNumber-1):
                 print(textwrap.dedent(f"""\
                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}
                """))
            if(tries > protagonist.tryNumber):
                print(textwrap.dedent(f"""\
                    - Core: SE TERMINÓ EL JUEGO :( 
                """))
                return
    print(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}

            """))            
# FIN DEL PRIMER PLANETA

          



    


# ------------------------------------------------------------------------------

"""
    Esta parte de abajo es la parte de ejecucuón del juego, es decir, la parte "MAIN"
"""
printInit()
playerChoice =  input("Ingrese su decisión: ").lower().strip()
while playerChoice[0] != "s":
    if(playerChoice[0] == "j"):
        print("Se iniciará el juego. Prepárate para una gran aventura!\n")
        game()
    elif(playerChoice[0] == "a"):
        printHelp()
    elif(playerChoice[0] == "c"):
        printCredits()
    printInit()
    playerChoice = input("Ingrese su decisión: ").lower().strip()

if(playerChoice[0]=="s"):
    print("\nAdiós, aventurero!\n")
    quit()

    


    