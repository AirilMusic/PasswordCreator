import random
import time
# work in progress

#pokemons:
class chorizord():
    def __init__(self):
        self.name = "Chorizord"
        self.tipo = "fuego"
        self.mivida = 78
        self.vidarival = 78
        self.defensa = 84
        self.ataque = 109
        self.velocidad = 1000

class blastheez():
    def __init__(self):
        self.name = "Blastheez"
        self.tipo = "agua"
        self.frase_especial = "blast theez nuts, mmmm..." #cuando salga de la pokebal dira esta frase en vez de su nombre
        self.mivida = 79
        self.vidarival = 79
        self.defensa = 105
        self.ataque = 85
        self.velocidad = 78

class bulbasaurio():
    def __init__(self):
        self.name = "Bulbasaurio"
        self.tipo = "planta"
        self.mivida = 45
        self.vidarival = 45
        self.defensa = 65
        self.ataque = 65
        self.velocidad = 45

class gardeguarra():
    def __init__(self):
        self.name = "Gardeguarra"
        self.tipo = "psiquico"
        self.mivida = 68
        self.vidarival = 68
        self.defensa = 115
        self.ataque = 125
        self.velocidad = 80

class poochyperro():
    def __init__(self):
        self.name = "Poochyperro"
        self.tipo = "siniestro"
        self.mivida = 35
        self.vidarival = 35
        self.defensa = 35
        self.ataque = 55
        self.velocidad = 35

class inferpene():
    def __init__(self):
        self.name = "Inferpene"
        self.tipo = "lucha"
        self.mivida = 76
        self.vidarival = 76
        self.defensa = 71
        self.ataque = 104
        self.velocidad = 108

pok1 = chorizord()
pok2 = blastheez()
pok3 = bulbasaurio()
pok4 = gardeguarra()
pok5 = poochyperro()
pok6 = inferpene()

pokemonEnCombate = pok1
pokRivalEnCombate = pok1
pokemonsVivos = 6
pokRivalVivos = 6

atacado = False

#ataques:
def atacar():
    print("¿Qué ataque quieres usar?\n", "1-asesinato    2-curita\n", "3-rapidin    4-tanque\n", "5-atras\n")
    ataque = input("Opción: ")
    ataqueRival = random.randint(1,4)
    
    if ataque == "5" or ataque.lower() == "atras":
        atacado = False
        
    elif ataque.lower() == "rapidin" or pokemonEnCombate.velocidad >= pokRivalEnCombate.velocidad and ataqueRival != 3:
        if ataque == "1" or ataque.lower() == "asesinato" and ataqueRival != 4:
            print("¡Has usado un ataque de asesinato!\n")
            pokRivalEnCombate.vidarival -= (100 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
        elif ataque == "2" or ataque.lower() == "curita" and ataqueRival != 4:
            print("¡Has usado un ataque de curita!")
            pokRivalEnCombate.vidarival -= (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
            pokemonEnCombate.vidarival += (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
            print("Tu pokamion se ha curado ", (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2), " puntos de vida\n")
        elif ataque == "3" or ataque.lower() == "rapidin" and ataqueRival != 4:
            print("¡Has usado un ataque de rapidin!\n")
            pokRivalEnCombate.vidarival -= (25 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
        elif ataque == "4" or ataque.lower() == "tanque" and ataqueRival != 4:
            print("¡Has usado un ataque de tanque!")
            print("Tu pokemon ha aguantado el ataque rival\n")
                
        if ataque != "4" or ataque.lower() != "tanque":
            if ataqueRival == 1:
                print("¡El rival ha usado un ataque de asesinato!\n")
                pokemonEnCombate.mivida -= (100 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
            elif ataqueRival == 2:
                print("¡El rival ha usado un ataque de curita!\n")
                pokemonEnCombate.mivida -= (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
                pokRivalEnCombate.vidarival += (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
                print("El pokamion rival se ha curado", (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2), " puntos de vida\n")
            elif ataqueRival == 3:
                print("¡El rival ha usado un ataque de rapidin!\n")
                pokemonEnCombate.mivida -= (25 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa)
            elif ataqueRival == 4:
                print("¡El rival ha usado un ataque de tanque!")
                print("El rival ha aguantado tu ataque\n")
        atacado = True

    else:
        if ataqueRival == 1:
            print("¡El rival ha usado un ataque de asesinato!\n")
            pokemonEnCombate.mivida -= (100 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
        elif ataqueRival == 2:
            print("¡El rival ha usado un ataque de curita!\n")
            pokemonEnCombate.mivida -= (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
            pokRivalEnCombate.vidarival += (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
            print("El pokamion rival se ha curado", (50 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2), " puntos de vida\n")
        elif ataqueRival == 3:
            print("¡El rival ha usado un ataque de rapidin!\n")
            pokemonEnCombate.mivida -= (25 + pokRivalEnCombate.ataque) - int(pokemonEnCombate.defensa/2)
        elif ataqueRival == 4:
            print("¡El rival ha usado un ataque de tanque!")
            print("El rival ha aguantado tu ataque\n")
                
        if ataque != "4":
            if ataque == "1" or ataque.lower() == "asesinato" and ataqueRival != 4:
                print("¡Has usado un ataque de asesinato!\n")
                pokRivalEnCombate.vidarival -= (100 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
            elif ataque == "2" or ataque.lower() == "curita" and ataqueRival != 4:
                print("¡Has usado un ataque de curita!")
                pokRivalEnCombate.vidarival -= (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
                pokemonEnCombate.vidarival += (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
                print("Tu pokamion se ha curado ", (50 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2), " puntos de vida\n")
            elif ataque == "3" or ataque.lower() == "rapidin" and ataqueRival != 4:
                print("¡Has usado un ataque de rapidin!\n")
                pokRivalEnCombate.vidarival -= (25 + pokemonEnCombate.ataque) - int(pokRivalEnCombate.defensa/2)
            elif ataque == "4" or ataque.lower() == "tanque" and ataqueRival != 4:
                print("¡Has usado un ataque de tanque!")
                print("Tu pokemon ha aguantado el ataque rival\n")
        atacado = True

#Cambiar de pokemon
def cambiarPokemon(quien):
    if quien == "jugador":
        print("¿A que pokemon quiere cambiar?\n", "1.Chorizord\n", "2.Blastheez\n", "3.Bulbasaurio\n", "4.Gardeguarra\n", "5.Poochyperro\n", "6.Inferpene\n", "7.Atras\n")
        opcion = input("Opción: ")
        if opcion != "7" or opcion.lower() != "atras":
            vez = 0
            while vez == 0 or pokemonEnCombate.mivida <= 0:
                if opcion == "1" or opcion.lower() == "chorizord":
                    pokemonEnCombate = pok1
                if opcion == "2" or opcion.lower() == "blastheez":
                    pokemonEnCombate = pok2
                if opcion == "3" or opcion.lower() == "bulbasaurio":
                    pokemonEnCombate = pok3
                if opcion == "4" or opcion.lower() == "gardeguarra":
                    pokemonEnCombate = pok4
                if opcion == "5" or opcion.lower() == "poochyperro":
                    pokemonEnCombate = pok5
                if opcion == "6" or opcion.lower() == "inferpene":
                    pokemonEnCombate = pok6
                vez = 1
            print("Tu pokemon ha cambiado a: ", pokemonEnCombate.name)
            if pokemonEnCombate.name == "Blastheez":
                print("Blast theez nuts, mmmm...\n") 
            atacado = True
                
    else:
        vez = 0
        while int(pokRivalEnCombate.vidarival) <= 0 or vez == 0:
            if pokRivalEnCombate.name == "Chorizord":
                pokRivalEnCombate = random.choice(pok2, pok3, pok4, pok5, pok6)
            elif pokRivalEnCombate.name == "Blastheez":
                pokRivalEnCombate = random.choice(pok1, pok3, pok4, pok5, pok6)
            elif pokRivalEnCombate.name == "Bulbasaurio":
                pokRivalEnCombate = random.choice(pok1, pok2, pok4, pok5, pok6)
            elif pokRivalEnCombate.name == "Gardeguarra":
                pokRivalEnCombate = random.choice(pok1, pok2, pok3, pok5, pok6)
            elif pokRivalEnCombate.name == "Poochyperro":
                pokRivalEnCombate = random.choice(pok1, pok2, pok3, pok4, pok6)
            elif pokRivalEnCombate.name == "Inferpene":
                pokRivalEnCombate = random.choice(pok1, pok2, pok3, pok4, pok5)
            vez = 1
        print("El rival ha cambiado de pokemon a: ", pokRivalEnCombate.name)
        if pokRivalEnCombate.name == "Blastheez":
            print("Blast theez nuts, mmmm...\n")

#Combate
while pokemonsVivos > 0 or pokRivalVivos > 0:
    atacado = False
    print("Tu pokemon es: ", pokemonEnCombate.name, " : ", pokemonEnCombate.mivida, "PV")
    print("El pokemon rival es: ", pokRivalEnCombate.name, " : ", pokRivalEnCombate.vidarival, "PV")
    while atacado == False:
        print("¿Que quieres hacer?\n", "1.Atacar\n", "2.Cambiar pokemon\n")
        opcion1 = input("Opción: ")
        if opcion1 == "1" or opcion1.lower() == "atacar":
            atacar()
        
        elif opcion1 == "2" or opcion1.lower() == "cambiar pokemon":
            cambiarPokemon("jugador")
        
        else:
            print("Opción no valida\n", "Vuelve a intentarlo\n")
        
        if pokemonEnCombate.vidarival <= 0:
            print("Tu pokemon ha muerto\n")
            cambiarPokemon("jugador")
            pokemonsVivos -= 1
        if pokRivalEnCombate.vidarival <= 0:
            print("El pokemon rival ha muerto\n")
            cambiarPokemon("rival")
            pokRivalVivos -= 1
    time.sleep(10)

if pokemonsVivos == 0:
    print("Has perdido")
else:
    print("Has ganado")
