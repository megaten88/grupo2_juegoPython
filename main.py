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
            / o       o \j
           /   \     /   \j
          /     )-"-(     \j
         /     ( 6 6 )     \j
        /       \ " /       \j
       /         )=(         \j
      /   o   .--"-"--.   o   \j
     /    I  /  -   -  \  I    \j
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
    questions =  createQuestions('lenguaje')
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
    questions = []
    # FIN DEL PRIMER PLANETA

     # Aquí empieza el segundo planeta

    planet,villain = createPlanet("Planeta Ingenio", "ingenio", "Sora")
    print(textwrap.dedent(f"""\
        *************LLEGANDO A {planet.name}
        - Arita: Veo que lo has logrado Core, encontrar al terrícola no era una tarea fácil.
        - Arita: Y mucho menos al indicado, tu fascinación por la exploración y el espacio; te ha traído muchos beneficios…
        - Arita: y sobre todo una gran responsabilidad.
        - Arita: Ser parte de este universo hasta el final de sus tiempos es tu destino como tu elección.

        - Arita: {protagonist.name} confía en el gran corazón e intuición de Core y pide su ayuda cuando mas la necesites.
        - Arita: El te ayudara a explorar el poder detrás de los objetos especiales.

        - {villain.name}: haber roto los sellos no te asegura este objeto especial, aun queda una ultima prueba por superar.
        - {villain.name}: Lee dos veces antes de contestar o la respuesta incorrecta podrías seleccionar.

            """))
    questions =  createQuestions('ingenio')
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
    questions = []
    # FIN DEL SEGUNDO PLANETA

    #AQUÍ COMIENZA EL TERCER PLANETA
    planet,villain = createPlanet("Planeta Ciencia", "ciencia", "Dernas")
    print(textwrap.dedent(f"""\
        *************LLEGANDO A {planet.name}
        - Core: ¡Wow! Mira {protagonist.name}, este es mi planeta favorito, donde ser un explorador no es...
        - Core: sinónimo de bandido, dudar es siempre la primera opción y equivocarse es solo el motivo para volverlo a intentar.
        - Core: Sabes, un día mi sueño fue pertenecer a este lugar. Ahora lo sé, mi destino era algo mas grande.
        - Core: ¡Vamos por esas preguntas!

        - {villain.name}: El llegar hasta esta etapa merece un reconocimiento, no cualquiera rompe nuestros sellos.
        - {villain.name}: Y para este momento ya han observado, analizado y experimentado, así que, es momento de la conclusión.
        - {villain.name}: Una prueba final que les permitirá obtener el resultado: el objeto especial que tanto buscan.

            """))
    questions =  createQuestions('ciencia')
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
    questions = []
    # FIN DEL TERCER PLANETA






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
