#Made by Ainhoa (Airil for discord and social media people)
import time
import random

print("SORTEO.uwu")
print("Hay dos tipos de sorteos, el normal y la ruleta rusa, ya cada uno que le ponga sus propias reglas")

while True:
    timer=5

    print("\nQue quieres hacer:", "\n-Normal", "\n-Ruleta Rusa")
    elecModJuego=input()

    if elecModJuego.lower()=="normal":
        print("\nA continuacion le saldran dos opciones (añadir persona y comnzar sorteo), dale a añadir persona hasta añadir todaslas personas del sorteo y seguidamente dale a comenzar sorteo.")

        jugadores=[]
        def añadir_persona():
            persona=input("Escriba el nombre de la persona: ")
            jugadores.append(persona)
        
        añadir_persona()
        numJugadores=int(1)

        empezar=False
        while empezar==False:
            print("\nQue quiere hacer ahora:", "\n-Añadir persona", "\n-Comenzar sorteo")
            opcion=input()

            if opcion.lower()=="añadir persona":
                añadir_persona()
                numJugadores=numJugadores+1

            elif opcion.lower()=="comenzar sorteo":
                print("\nCOMIENZA EL SORTEO...")
                print("El ganador es: ", jugadores[random.randint(0, numJugadores-1)])
                empezar=True

            else:
                print("¡Error! La opcion esta mal escrita, por favor vuelva a escribirla")
        timer=4

    elif elecModJuego.lower()=="ruleta rusa":
        print("\nA continuacion se le pedira que escriba el numero de jugadores que hay en la mesa y la cantidad de balas en el cargador(1-6), despues cada jugador tendra que dispararse una vez y pasarle el turno al siguiente, hasta que no queden balas en el cargador.")
        jugadores=int(input("\nNumero de jugadores: "))
        cargador=(1,2,3,4,5,6)
        balas=0
        balas=int(input("Numero de balas (1-6): "))
        while balas < 1 and balas > 6:
            balas=int(input("Numero de balas (1-6): "))

        while balas > 0:
            print("\npulse enter para disparar")
            disparar=input("¡DISPARAR!")

            suerte=random.randint(1,6)
            if suerte > balas:
                print("\n¡Felicidades! se te ha perdonado la vida hasta la siguiente ronda")
            
            else:
                print("\n¡PUM!")
                balas=balas-1
                jugadores=jugadores-1
            
            if jugadores==0:
                balas=0
                print("Murieron todos los jugadores...")
        
        print("SE TERMINO EL JUEGO")
        timer=4

    else:
        print("\nAlgo salio mal, vuelva a escribir el tipo de sorteo.")
        timer=2
    
    time.sleep(timer)
