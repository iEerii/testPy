title = "Bienvenido al quiz de Harry Potter"
print("\n" + title + "\n" + "*" * len(title) + "\n")

score = 0
wrongAnswer = 0

def options(option, right):
    global score, wrongAnswer
    if option == right: score += 5
    else: wrongAnswer += 1

option = input("""Pregunta 1 ¿Cuando Harry va a comprar su varita en Ollivander's 
                ¿De qué es el núcleo de la varita?
                a) Saliva de basilisco
                b) Pluma de fenix 
                c) Escama de colacuerno hungaro 
                d) Pelo de centauro
                Respuesta: """)
options(option, "b")

option = input("""Pregunta 2 Cuando Harry Potter se pone el sombrero seleccionador, 
                pide en voz baja que no lo mande a una de las casas. ¿Cuál?
                a) Gryffindor
                b) Ravenclaw
                c) Huffelpuff
                d) Slytherin
                Respuesta: """)
options(option, "d")

option = input("""Pregunta 3 Cuando Hermione conoce a Harry y a Ron en el Expreso de Hogwarts, 
                les muestra un hechizo que aprendió. ¿Cual es?
                a) Alohomora
                b) Accio
                c) Occulus Reparo
                d) Sectumsempra
                Respuesta: """)
options(option, "c")

option = input("""Pregunta 4 ¿Cuál es la escoba voladora que recibe Harry en su primer año?
                a) Nimbus 2000 
                b) Saeta de fuego
                c) Barredora 5
                d) Cometa 360 
                Respuesta: """)
options(option, "a")

option = input("""Pregunta 5 ¿Quien es aquel que no se puede nombrar?
                a) Dobby
                b) Sirius black
                c) Lord Voldemort
                d) Peter Pettigrew
                Respuesta: """)
options(option, "c")

if score <= 5:
    print("Tu puntaje es de {} puntos, te falta calle Diagon. Fallaste todas, muggle"
          .format(score, wrongAnswer))
elif score >5 and score <=20: 
    print("Tu puntaje es de {} puntos, ¡A estudiar como Hermione! Fallaste {} preguntas"
        .format(score, wrongAnswer))
else:
    print("¡Caracoles hervidos! Obtuviste {} puntos, vaya que estas expuest@ a Harry Potter"
          .format(score))
        