##Work in progress

import random
import time

pokemons = {
    "Charizard": "Fire", 
    "Squirtle": "Water", 
    "Bulbasaur": "Grass", 
    "Charmander": "Fire", 
    "Pikachu": "Electric", 
    "Pidgeot": "Flying", 
    "Snorlax": "Normal", 
    "Magikarp": "Water", 
    "Eevee": "Normal", 
    "Jigglypuff": "Normal", 
    "Mew": "Psychic", 
    "Mewtwo": "Psychic", 
    "Oddish": "Grass",
    "Pidgeotto": "Flying",
    "Pidgey": "Flying",
    "Rattata": "Normal",
    "Scyther": "Bug",
    "Vulpix": "Fire",
    "Weedle": "Bug",
    "Zubat": "Poison"
}

ataques = {
    "Combate" : ["Normal", 35],
    "Ala de acero" : ["Acero", 11],
    "Cola dragon" : ["Dragon", 15],
    "Cola Ferrea" : ["Acero", 15],
    "Lanzarrocas" : ["Roca", 12],
    "Colmillo Igneo" : ["Fuego", 12],
    "Contraataque" : ["Lucha", 12],
    "Cascada" : ["Agua", 16],
    "Antiaereo" : ["Roca", 16],
    "Hoja afilada" : ["Planta", 13],
    "Bofeton lodo" : ["Tierra", 18],
    "Giro fuego" : ["Fuego", 14],
    "Calcinacion" : ["Fuego", 29],
    "Arañazo" : ["Normal", 6],
    "Latigo cepa" : ["Planta", 7],
    "Destructor" : ["Normal", 7],
    "Tajo aereo" : ["Volador", 14],
    "Golpe roca" : ["Lucha", 15], 
    "Garra metal" : ["Acero", 8], 
    "Picadura" : ["Bicho", 5],
    "Ascuas" : ["Fuego", 10],
    "Ataque rapido" : ["Normal", 8],
    "Placaje" : ["Normal", 10],
    "Corte" : ["Normal", 10],
    "Pistola agua" : ["Agua", 10],
    "Burbuja" : ["Agua", 12],
    "Estoicismo" : ["Bicho", 15],
    "Acoso" : ["Bicho", 10],
    "Voltiocambio" : ["Electrico", 14],
    "Chispas" : ["Electrico", 6],
    "Impactrueno" : ["Electrico", 5],
    "Disparo lodo" : ["Tierra", 5]
}

#mi cinturon
class mi1():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
        
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class mi2():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))
        
class mi3():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))
        
class mi4():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class mi5():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class mi6():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

miPoke1 = mi1()
miPoke2 = mi2()
miPoke3 = mi3()
miPoke4 = mi4()
miPoke5 = mi5()
miPoke6 = mi6()

miPokeEnCombate = miPoke1

#cinturon del rival
class en1():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class en2():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))
        
class en3():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))
        
class en4():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class en5():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

class en6():
    def __init__(self):
        shinyRNG = random.randint(1, 2**13)
        if shinyRNG == 1:
            self.shiny = True
        else:
            self.shiny = False
            
        self.pokenum = random.randint(0, len(pokemons) - 1)
        self.pokemon = list(pokemons.keys())[self.pokenum]
        self.tipo = list(pokemons.values())[self.pokenum]
        
        self.ivVida = random.randint(0, 31)
        self.ivAtaque = random.randint(0, 31)
        self.ivAtaqueEspecial = random.randint(0, 31)
        self.ivDefensa = random.randint(0, 31)
        self.ivDefensaEspecial = random.randint(0, 31)
        self.ivVelocidad = random.randint(0, 31)
        
        self.ataque1 = random.randint(0, len(ataques) - 1)
        self.ataque2 = random.randint(0, len(ataques) - 1)
        self.ataque3 = random.randint(0, len(ataques) - 1)
        self.ataque4 = random.randint(0, len(ataques) - 1)
        
        self.vida = self.ivVida + self.ivDefensa + self.ivDefensaEspecial + int(random.randint(200, 400))

PokeEn1 = en1()
PokeEn2 = en2()
PokeEn3 = en3()
PokeEn4 = en4()
PokeEn5 = en5()
PokeEn6 = en6()

pokRivalEnCombate = PokeEn1

#acciones
daño = 0
def atacar(quien, ataque):
    if int(ataque) == 1:
        if quien == "jugador":
            daño = miPokeEnCombate.ivAtaque + miPoke1.ivAtaqueEspecial + int((list(ataques.values())[miPokeEnCombate.ataque1])[1])
            pokRivalEnCombate.vida = pokRivalEnCombate.vida - daño
            if str(miPokeEnCombate.tipo) == str((list(ataques.values())[miPokeEnCombate.ataque1])[1]):
                daño = daño * 1.5
        else:
            daño = pokRivalEnCombate.ivAtaque + pokRivalEnCombate.ivAtaqueEspecial + int((list(ataques.values())[pokRivalEnCombate.ataque1])[1])
            miPokeEnCombate.vida = miPokeEnCombate.vida - daño
            if str(pokRivalEnCombate.tipo) == str((list(ataques.values())[pokRivalEnCombate.ataque1])[1]):
                daño = daño * 1.5
    
    elif int(ataque) == 2:
        if quien == "jugador":
            daño = miPokeEnCombate.ivAtaque + miPoke1.ivAtaqueEspecial + int((list(ataques.values())[miPokeEnCombate.ataque2])[1])
            pokRivalEnCombate.vida = pokRivalEnCombate.vida - daño
            if str(miPokeEnCombate.tipo) == str((list(ataques.values())[miPokeEnCombate.ataque2])[1]):
                daño = daño * 1.5
        else:
            daño = pokRivalEnCombate.ivAtaque + pokRivalEnCombate.ivAtaqueEspecial + int((list(ataques.values())[pokRivalEnCombate.ataque2])[1])
            miPokeEnCombate.vida = miPokeEnCombate.vida - daño
            if str(pokRivalEnCombate.tipo) == str((list(ataques.values())[pokRivalEnCombate.ataque2])[1]):
                daño = daño * 1.5
    
    elif int(ataque) == 3:
        if quien == "jugador":
            daño = miPokeEnCombate.ivAtaque + miPoke1.ivAtaqueEspecial + int((list(ataques.values())[miPokeEnCombate.ataque3])[1])
            pokRivalEnCombate.vida = pokRivalEnCombate.vida - daño
            if str(miPokeEnCombate.tipo) == str((list(ataques.values())[miPokeEnCombate.ataque3])[1]):
                daño = daño * 1.5
        else:
            daño = pokRivalEnCombate.ivAtaque + pokRivalEnCombate.ivAtaqueEspecial + int((list(ataques.values())[pokRivalEnCombate.ataque3])[1])
            miPokeEnCombate.vida = miPokeEnCombate.vida - daño
            if str(pokRivalEnCombate.tipo) == str((list(ataques.values())[pokRivalEnCombate.ataque3])[1]):
                daño = daño * 1.5
    
    elif int(ataque) == 4:
        if quien == "jugador":
            daño = miPokeEnCombate.ivAtaque + miPoke1.ivAtaqueEspecial + int((list(ataques.values())[miPokeEnCombate.ataque4])[1])
            pokRivalEnCombate.vida = pokRivalEnCombate.vida - daño
            if str(miPokeEnCombate.tipo) == str((list(ataques.values())[miPokeEnCombate.ataque4])[1]):
                daño = daño * 1.5
        else:
            daño = pokRivalEnCombate.ivAtaque + pokRivalEnCombate.ivAtaqueEspecial + int((list(ataques.values())[pokRivalEnCombate.ataque4])[1])
            miPokeEnCombate.vida = miPokeEnCombate.vida - daño
            if str(pokRivalEnCombate.tipo) == str((list(ataques.values())[pokRivalEnCombate.ataque4])[1]):
                daño = daño * 1.5

def cambiarPokemon(quien, newpokemon):
    if quien.lower() == "jugador":
        if newpokemon.lower() == miPoke1.pokemon.lower():
            miPokeEnCombate = miPoke1
        elif newpokemon.lower() == miPoke2.pokemon.lower():
            miPokeEnCombate = miPoke2
        elif newpokemon.lower() == miPoke3.pokemon.lower():
            miPokeEnCombate = miPoke3
        elif newpokemon.lower() == miPoke4.pokemon.lower():
            miPokeEnCombate = miPoke4
        elif newpokemon.lower() == miPoke5.pokemon.lower():
            miPokeEnCombate = miPoke5
        elif newpokemon.lower() == miPoke6.pokemon.lower():
            miPokeEnCombate = miPoke6
            
        while miPokeEnCombate.vida <= 0:
            print("Ese pokemon esta muerto, por favor elige otro: ")
            print("\n", miPoke1.pokemon, " || ", miPoke1.tipo, "\n", miPoke2.pokemon, " || ", miPoke2.tipo, "\n", miPoke3.pokemon, " || ", miPoke3.tipo, "\n", miPoke4.pokemon, " || ", miPoke4.tipo, "\n", miPoke5.pokemon, " || ", miPoke5.tipo, "\n", miPoke6.pokemon, " || ", miPoke6.tipo, "\n")
            newpokemon = input("Pokemon: ")
            if newpokemon.lower() == miPoke1.pokemon.lower():
                miPokeEnCombate = miPoke1
            elif newpokemon.lower() == miPoke2.pokemon.lower():
                miPokeEnCombate = miPoke2
            elif newpokemon.lower() == miPoke3.pokemon.lower():
                miPokeEnCombate = miPoke3
            elif newpokemon.lower() == miPoke4.pokemon.lower():
                miPokeEnCombate = miPoke4
            elif newpokemon.lower() == miPoke5.pokemon.lower():
                miPokeEnCombate = miPoke5
            elif newpokemon.lower() == miPoke6.pokemon.lower():
                miPokeEnCombate = miPoke6
                
        print("\n Tu pokemon en combate ha cambiado a: ", miPokeEnCombate.pokemon)
    
    else: #rival, cambia una vez se muere un pokemon o sino va por una baja probabilidad que cambie de pokemon
        pokRivalEnCombate = random.choice([PokeEn1, PokeEn2, PokeEn3, PokeEn4, PokeEn5, PokeEn6])
        while pokRivalEnCombate.vida <= 0:
            pokRivalEnCombate = random.choice([PokeEn1, PokeEn2, PokeEn3, PokeEn4, PokeEn5, PokeEn6])
        print("\n El rival ha cambiado a: ", pokRivalEnCombate.pokemon)

#combate (creo XD)
while True:
    opcion = input("\n¿Qué quieres hacer?\n1. Atacar\n2. Cambiar Pokemon\n")
    vueltas = 0
    while opcion.lower() != "atacar" or opcion.lower() != "cambiar pokemon" and vueltas < 1:
        if opcion.lower() == "atacar" or opcion == "1":
            print("\nResponde con un número:")
            ataque = input("¿Qué ataque quieres usar?\n1. " + str(list(ataques.keys())[miPokeEnCombate.ataque1]) + " || " + str(list(ataques.values())[miPokeEnCombate.ataque1]) + "\n2. " + str(list(ataques.keys())[miPokeEnCombate.ataque2]) + " || " + str(list(ataques.values())[miPokeEnCombate.ataque2]) + "\n3. " + str(list(ataques.keys())[miPokeEnCombate.ataque3]) + " || " + str(list(ataques.values())[miPokeEnCombate.ataque3]) + "\n4. " + str(list(ataques.keys())[miPokeEnCombate.ataque4]) + " || " + str(list(ataques.values())[miPokeEnCombate.ataque4]) + "\n")
            quien = "jugador"
            atacar(quien, ataque)
            break #hacia cosas raras y con esto lo he arreglado sin necesidad de pensar :)
            
        elif opcion.lower() == "cambiar pokemon" or opcion == "2":
            quien = "jugador"
            print("\n", miPoke1.pokemon, " || ", miPoke1.tipo, "\n", miPoke2.pokemon, " || ", miPoke2.tipo, "\n", miPoke3.pokemon, " || ", miPoke3.tipo, "\n", miPoke4.pokemon, " || ", miPoke4.tipo, "\n", miPoke5.pokemon, " || ", miPoke5.tipo, "\n", miPoke6.pokemon, " || ", miPoke6.tipo, "\n")
            newpokemon = input("\nElige un pokemon: ")
            cambiarPokemon(quien, newpokemon)
            break
        
        else:
            print("Algo salio mal, vuelve a intentarlo")
            opcion = input("\n¿Qué quieres hacer?\n1. Atacar\n2. Cambiar Pokemon\n")
            
        vueltas = 1
    
    quien = "rival"
    if pokRivalEnCombate.vida <= 0:
        print("\nEl pokemon rival esta debilitado")
        cambiarPokemon(quien, pokRivalEnCombate.pokemon)
        print(pokRivalEnCombate.pokemon)
    
    ataqueRival = random.randint(1, 4)
    atacar(quien, ataqueRival)
    print("\nEl rival ha usado: ", list(ataques.keys())[ataqueRival])
    
    print("\nTu ", miPokeEnCombate.pokemon," tiene: ", miPokeEnCombate.vida, " de vida", "\nEl ", pokRivalEnCombate.pokemon ," rival tiene: ", pokRivalEnCombate.vida, " de vida")
    
    quien = "jugador"
    if miPokeEnCombate.vida <= 0:
        print("\nTu pokemon esta debilitado")
        print("\n", miPoke1.pokemon, " || ", miPoke1.tipo, "\n", miPoke2.pokemon, " || ", miPoke2.tipo, "\n", miPoke3.pokemon, " || ", miPoke3.tipo, "\n", miPoke4.pokemon, " || ", miPoke4.tipo, "\n", miPoke5.pokemon, " || ", miPoke5.tipo, "\n", miPoke6.pokemon, " || ", miPoke6.tipo, "\n")
        newpokemon = input("\nElige un pokemon: ")
        cambiarPokemon(quien, newpokemon)
        print(miPokeEnCombate.pokemon)