titulo = "Bienvenido al quiz de Harry Potter"
print("\n" + titulo + "\n" + "*" * len(titulo) + "\n")

puntaje = 0

opcion = input("""Pregunta 1 ¿Cuando Harry va a comprar su varita en Ollivander's 
                ¿De qué es el núcleo de la varita?
                a) Saliva de basilisco
                b) Pluma de fenix 
                c) Escama de colacuerno hungaro 
                d) Pelo de centauro
                Respuesta: """)
if opcion == "b": puntaje += 5

opcion = input("""Pregunta 2 Cuando Harry Potter se pone el sombrero seleccionador, 
                pide en voz baja que no lo mande a una de las casas. ¿Cuál?
                a) Gryffindor
                b) Ravenclaw
                c) Huffelpuff
                d) Slytherin
                Respuesta: """)
if opcion == "d": puntaje += 5

opcion = input("""Pregunta 3 Cuando Hermione conoce a Harry y a Ron en el Expreso de Hogwarts, 
               |les muestra un hechizo que aprendió. ¿Cual es?
                a) Alohomora
                b) Accio
                c) Occulus Reparo
                d) Sectumsempra
                Respuesta: """)
if opcion == "c": puntaje += 5

opcion = input("""Pregunta 4 ¿Cuál es la escoba voladora que recibe Harry en su primer año?
                a) Nimbus 2000 
                b) Saeta de fuego
                c) Barredora 5
                d) Cometa 360 
                Respuesta: """)
if opcion == "a": puntaje += 5

opcion = input("""Pregunta 5 ¿Quien es aquel que no se puede nombrar?
                a) Dobby
                b) Sirius black
                c) Lord Voldemort
                d) Peter Pettigrew
                Respuesta: """)
if opcion == "c": puntaje += 5