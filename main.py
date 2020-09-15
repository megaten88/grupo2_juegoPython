from  pregunta import *
from  classes import *
import textwrap
import sys #nuevo
import time #nuevo

#Formato de texto
wrapper = textwrap.TextWrapper(width = 100,replace_whitespace=False)
def text_format(message):
            wrapped_text = wrapper.fill(text=message)
    #for index in range(len(wrapped_text)):
    #    for elem in wrapped_text[index]:
            for character in wrapped_text: #nuevo
                sys.stdout.write(character) #nuevo
                sys.stdout.flush() #nuevo
                time.sleep(0.03) #nuevo
            print("")



"""
    Esta parte es donde definimos lo que usaremos en el juego.
"""

def printInit():
    print('\n'*3) #nuevo
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
    message = "Si estás leyendo este mensaje debes ser el terrícola que he buscado durante tanto tiempo. Dime, ¿Cuál es tu nombre?"
    text_format(message)

    name = input("Ingresa el nombre del personaje: ")
    protagonist = Protagonist(name,1,1)

    text_format(textwrap.dedent(f"""
        {protagonist.name} ¡perfecto! Mucho gusto, mi nombre es Core y nadie conoce este lado del universo mejor que yo, o al menos eso es lo que dicen jeje.
        - Core: Ohh amigo, te ves algo perdido…
        - Core: Hmmmmmmmmm,, ¿que te parece si te unes a mi mas reciente y emocionante misión? Te explicare mas en el camino, ¡vamos!
        .
        .
        .
            """))
    playerChoice = input("**¿Viajar junto a Core?\n [Sí(S)/No(N)]: ").lower().strip()
    if(playerChoice[0]=="n"):
        text_format("Core: Está bien, entiendo, espero verte pronto amigo.")
        return
    text_format(textwrap.dedent(f"""\
        - Core: Gracias por acompañarme en esta aventura, te explico.\n
        - Core: Nuestra misión es recolectar los 5 objetos especiales cada uno se encuentra resguardado por un guardián de planeta. Y para llegar a el debemos romper los sellos que los protegen ¿de que manera?\n
        - Core: Pues respondiendo de forma correcta una serie de preguntas que nos harán debemos tener mucho cuidado pues si fallamos mas de 3 veces seremos descubiertos y exiliados del planeta.\n
        - Core: Yo confió plenamente en tus habilidades, pero si te sientes en demasiados problemas puedo ayudarte recuerda que somos compañeros, ante todo.\n
        - Core: Cada planeta nos dará por su nombre la pista de que tipo de trivia o acertijo podremos encontrar en el, así que adelante y comencemos con el planeta del Lenguaje…\n

            """))

 # Aquí empieza la dinámica para todos los planetas
    planet,villain = createPlanet("Planeta Lenguaje", "lenguaje", "Sir.Lovial")
    text_format(textwrap.dedent(f"""\
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
                 text_format(textwrap.dedent(f"""\

                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}

                """))
            if(tries > protagonist.tryNumber):
                text_format(textwrap.dedent(f"""\

                    - Core: SE TERMINÓ EL JUEGO :(

                """))
                return
    text_format(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}



            """))
    questions = []
    # FIN DEL PRIMER PLANETA

# Aquí empieza el segundo planeta

    planet,villain = createPlanet("Planeta Ingenio", "ingenio", "Sora")
    text_format(textwrap.dedent(f"""\
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
                 text_format(textwrap.dedent(f"""\
                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}
                """))
            if(tries > protagonist.tryNumber):
                text_format(textwrap.dedent(f"""\
                    - Core: SE TERMINÓ EL JUEGO :(
                """))
                return
    text_format(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}

            """))
    questions = []
    # FIN DEL SEGUNDO PLANETA

    #AQUÍ COMIENZA EL TERCER PLANETA
    planet,villain = createPlanet("Planeta Ciencia", "ciencia", "Dernas")
    text_format(textwrap.dedent(f"""\


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
                 text_format(textwrap.dedent(f"""\
                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}
                """))
            if(tries > protagonist.tryNumber):
                text_format(textwrap.dedent(f"""\
                    - Core: SE TERMINÓ EL JUEGO :(
                """))
                return
    text_format(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}

            """))
    questions = []
    # FIN DEL TERCER PLANETA

#AQUÍ COMIENZA EL CUARTO PLANETA
    planet,villain = createPlanet("Planeta Cultura General", "cultura", "Soldish")
    text_format(textwrap.dedent(f"""\


        *************LLEGANDO A {planet.name}
        - Core: el ser un explorador me ha enseñado tantas cosas, 
        - Core: he aprendido lo importante que es la función de todos en el universo, ningún conocimiento vale menos que el de otros, y que todos tenemos algo que entregar.
        - Core: Yo vengo de un planeta llamado foody.  Hablamos de los mejores cocineros del universo, la mayor diversidad en alimentos que este pueda entregar.
        - Core: pero yo jamás lo entendí o jamás pertenecí ahí. No lo se… 
        - Core: Desde muy joven me apasione por la exploración espacial es lo único que conocía y ahora estoy contigo en esta misión. 
        - Core: La mas importante de mi vida, conozco el espacio, mi misión y a mi amigo que acompaña. 

        - {villain.name}: impresionante, lograron romper los sellos
        - {villain.name}: Pero eso no basta para obtener mi objeto especial, así que, llego la hora de la prueba final,
        - {villain.name}: ¿que tanto saben acerca de todo lo que se puede saber? 



            """))
    questions =  createQuestions('cultura')
    for question in questions:
        correct = None
        tries=0
        while(correct is None and tries<= protagonist.tryNumber):
            correct = answer_check(question,protagonist)
            if(correct is None ):
                tries+=1
            if(tries == protagonist.tryNumber-1):
                 text_format(textwrap.dedent(f"""\
                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}
                """))
            if(tries > protagonist.tryNumber):
                text_format(textwrap.dedent(f"""\
                    - Core: SE TERMINÓ EL JUEGO :(
                """))
                return
    text_format(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}

            """))
    questions = []
    # FIN DEL CUARTO PLANETA

#AQUÍ COMIENZA EL QUINTO PLANETA
    planet,villain = createPlanet("Planeta Logico-Matematico", "logico-matematico", "Minus")
    text_format(textwrap.dedent(f"""\

        
        *************LLEGANDO A {planet.name}
        - Core: Desde que Minus el guardián del objeto de este planeta se ha plantado aquí, ya nada es igual.
        - Core: Sus habitantes no son felices. 
        - Core: Su necesidad de abarcar el poder y conocimiento de los demás dejo desestabilizada esta parte del universo. 
        - Core: El alguna vez junto los objetos especiales también, pero no pudo usarlos de manera correcta y creo un desequilibro. 
        - Core: Pero tu {protagonist.name} tienes todo lo que se necesita, y podrás recobrar el equilibrio, se debe sentir muy genial ser tan fundamental ¿no? ¡vamos! Ya solo falta un poco mas amigo.
        
        - {villain.name}: ¡Por fin! el ultimo de los foody´s y el terrícola que tuvo que conseguir, es una lastima que estuvieras en exploración justo en el momento que decidí absorber y colisionar todo tu planeta, no estaríamos en esta situación… 
        - {villain.name}: El hecho que ustedes dos pudieran superar los demás planetas, obtener los objetos y romper mis sellos no les asegura nada, no será para nada sencillo.
        - {villain.name}: Prepárense para la prueba final…
        

            """))
    questions =  createQuestions('logico-matematico')
    for question in questions:
        correct = None
        tries=0
        while(correct is None and tries<= protagonist.tryNumber):
            correct = answer_check(question,protagonist)
            if(correct is None ):
                tries+=1
            if(tries == protagonist.tryNumber-1):
                 text_format(textwrap.dedent(f"""\
                    - Core: Te ayudaré un poquito! La pista de esta pregunta es: {question.hint}
                """))
            if(tries > protagonist.tryNumber):
                text_format(textwrap.dedent(f"""\
                    - Core: SE TERMINÓ EL JUEGO :(
                """))
                return
    text_format(textwrap.dedent(f"""\
        - {villain.name}: Me has vencido, {protagonist.name}.

        RESUMEN DEL PROTAGONISTA:
        {protagonist}

            """))
    questions = []
    # FIN DEL QUINTO PLANETA

#FIN DEL JUEGO
    text_format(textwrap.dedent(f"""\
        
        ¡Felicidades! Has completado el modo historia del juego. 

         Vemos como se comienzan a formar planetas que no habíamos visto. Una imagen indescriptiblemente hermosa. 
         Y que, si eran aquellos que habían sido absorbidos por la avaricia de Minus. 
         El equilibrio estaba de vuelta...

        - Core: ... Amigo, lo hemos logrado. Gracias por traer de vuelta mi planeta y regalarme un hogar eterno, jamás lo olvidare.
        - Core: Ni tu a mi, por que siempre que veas al hacia el espacio y estés en busca de una nueva aventura ahí estaré yo, apoyándote. 
        - Core: Hasta siempre.

        Jamás Core se Había visto mas feliz, por fin había encontrado el lugar al que pertenecía y no estaba solo. (Core se desvanece poco a poco en el espacio)

        - Arita: {protagonist.name} Core jamás se sintió parte de su planeta, pero eso no quiere decir que no lo amara, cuando el se entero de la absorción de inmediato fue a mi planeta, y descubrió que la única manera de regresar el equilibrio era juntando de nuevo los objetos especiales. 
        - Arita: Volver a ese espacio-tiempo. Pero solo un terrícola seria capaz de manejar ese poder, de ayudarlo a completar esa misión, esa obsesión lo llevo hacia ti. 
        - Arita: El precio era demasiado alto y el lo sabia. Su existencia ya no seria la misma, debería unir su materia y ser al espacio. 
        - Arita: Fue difícil de aceptar, pero con el tiempo comprendió que ese era su verdadero hogar y el conocerte le dio su verdadera familia.
        - Arita: Ahora regresaras a tu planeta y encontraras tu verdadera misión como terrícola Tu memoria será borrada el momento antes de leer la carta de Core, pero tus sentimientos quedaran intactos.

        FIN

            """))
#fIN DEL JUEGO


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
