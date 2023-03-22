# https://www.hackerrank.com/challenges/maze-escape/problem

pid = input()
arr = [list(input()), list(input()), list(input())]

#primero mira si e esta en el campo de vision y si esta va hacia el
einarr = False
pose = [0, 0]
for y in range(3):
    if "e" in arr[y]:
        pose = [y, arr[y].index("e")]
        einarr = True
        break

#luego mira si hay paredes en el campo de vision, y si hay intenta si la pared es arriba, ir a la derecha, si es en la derecha va abajo, si es abajo va a la izquierda y si es en la izquierda va a arriba
winarr = False
for y in range(3):
    if "#" in arr[y]:
        winarr = True
        break
        
# depende lo que hay en el tablero hace una cosa u otra
if einarr == True:
    if arr[0][1] == "e":
        print("UP")
    elif arr[2][1] == "e":
        print("DOWN")
    elif arr[1][0] == "e":
        print("LEFT")
    elif arr[1][2] == "e":
        print("RIGHT")
    elif arr[0][0] == "e":
        if arr[0][1] != "#":
            print("UP")
        else:
            print("LEFT")
    elif arr[0][2] == "e":
        if arr[0][1] != "#":
            print("UP")
        else:
            print("RIGHT")
    elif arr[2][0] == "e":
        if arr[2][1] != "#":
            print("DOWN")
        else:
            print("LEFT")
    elif arr[2][2] == "e":
        if arr[2][1] != "#":
            print("DOWN")
        else:
            print("RIGT")

elif winarr == True:
    if arr[0][1] == "#":
        if arr[1][2] != "#":
            print("RIGHT")
        else:
            print("DOWN")
    elif arr[1][2] == "#":
        if arr[2][1] != "#":
            print("DOWN")
        else:
            print("LEFT")
    elif arr[2][1] == "#":
        if arr[1][0] != "#":
            print("LEFT")
        else:
            print("UP")  
    elif arr[1][0] == "#":
        if arr[0][1] != "#":
            print("UP")
        else:
            print("RIGHT")
    #ahora las 4 esquinas, si o si solo va ha haber un una esquina sin pared a partir de aqui, porque sino ya se hubiese computado
    elif arr[0][2] == "#":
        print("RIGHT")
    elif arr[2][2] == "#":
        print("DOWN")
    elif arr[2][0] == "#":
        print("LEFT")
    else:
        print("UP")
else:
    print("RIGHT")
