#################### BOMBpy GAME ####################
################### Made by Airil ###################

# Un juego que se pueda utilizar para examenes... la idea es un juego en el que haya una bomba y 4, 6 u 8 cables, entonces por pantalla se te mostrará un codigo, y tienes que entender el código para saber que cable cortar (o en caso de cortar mas de uno en que orden) y todo esto en un tiempo, la cantidad de cables depende del codigo que hay tres tipos de codigos (easy, medium y hard) y luego al configurar el juego/examen puedas poner una dificultad del 1 al 10 y entonces segun eso se asignara un numero de x easy, y medium y z hard, (en cada una de esas tres dificultades habra 10 codigos distintos y en cada uno hay una lista de habilidades que se tratan, y todo eso se guarda en estadisticas y al terminar el examen (10 ejercicios de 2, 4 o 6 minutos) se mostraran graficas de las estadisticas y la nota (y pese a que la dificultad esta determinada, los ejercicios se asignan de forma aleatoria)

import random
import time
import pygame
from termcolor import colored
import matplotlib

levels = {
    "easy":{
        "1":[[], # habilidades
            """

            """,
            [3]], # cable correcto (o cables, en el orden puesto)

        "2":[[], # habilidades
            """

            """,
            [1]], # cable correcto (o cables, en el orden puesto)

        "3":[[], # habilidades
            """

            """,
            [2]], # cable correcto (o cables, en el orden puesto)

        "4":[[], # habilidades
            """

            """,
            [4]], # cable correcto (o cables, en el orden puesto)

        "5":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "6":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "7":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "8":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "9":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "10":[[], # habilidades
            """

            """,
            []]}, # cable correcto (o cables, en el orden puesto)

    "medium":{
        "1":[[], # habilidades
            """

            """,
            [3]], # cable correcto (o cables, en el orden puesto)

        "2":[[], # habilidades
            """

            """,
            [6]], # cable correcto (o cables, en el orden puesto)

        "3":[[], # habilidades
            """

            """,
            [2]], # cable correcto (o cables, en el orden puesto)

        "4":[[], # habilidades
            """

            """,
            [4]], # cable correcto (o cables, en el orden puesto)

        "5":[[], # habilidades
            """

            """,
            [5]], # cable correcto (o cables, en el orden puesto)

        "6":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "7":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "8":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "9":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "10":[[], # habilidades
            """

            """,
            []]}, # cable correcto (o cables, en el orden puesto)

    "hard":{
        "1":[[], # habilidades
            """

            """,
            [8]], # cable correcto (o cables, en el orden puesto)

        "2":[[], # habilidades
            """

            """,
            [1]], # cable correcto (o cables, en el orden puesto)

        "3":[[], # habilidades
            """

            """,
            [2]], # cable correcto (o cables, en el orden puesto)

        "4":[[], # habilidades
            """

            """,
            [4]], # cable correcto (o cables, en el orden puesto)

        "5":[[], # habilidades
            """

            """,
            [7]], # cable correcto (o cables, en el orden puesto)

        "6":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "7":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "8":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "9":[[], # habilidades
            """

            """,
            []], # cable correcto (o cables, en el orden puesto)

        "10":[[], # habilidades
            """

            """,
            []]}} # cable correcto (o cables, en el orden puesto)

print(colored("""
██████╗  ██████╗ ███╗   ███╗██████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██╔████╔██║██████╔╝██████╔╝ ╚████╔╝ 
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔═══╝   ╚██╔╝  
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝██║        ██║   
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝        ╚═╝   
""", 'green'))

print(colored("Made by Airil/Ainhoara\n", 'cyan'))

difficulty = 0

while difficulty == 0:
    inp = input(colored("[-] Set difficulty level (1-10): ", 'green'))
    try:
        if int(inp) <= 10 and int(inp) >= 1:
            difficulty = int(inp)
        else:
            print(colored("[!] ERROR: difficulty must be a number between 1 and 10\n", 'red'))

    except:
        difficulty = 0
        print(colored("[!] ERROR: difficulty must be a number between 1 and 10\n", 'red'))

# asignar los niveles segun la dificultad
levels = []


# juego


# estadisticas y nota


