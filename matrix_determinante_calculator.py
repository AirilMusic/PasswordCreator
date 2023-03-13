import pyperclip

def determinante(rowlong, arr):
    res = " = "
    if rowlong == 1:
        res += str(arr[i][0])
    if rowlong == 2:
        res += str(arr[0][0]) + " * " + str(arr[0][1]) + " - " + str(arr[1][0]) + " * " + str(arr[1][1]) + " = " + str((arr[0][0] * arr[1][1]) - (arr[1][0] * arr[0][1]))
    if rowlong == 3:
        res += "(" + str(arr[0][0]) + " * " + str(arr[1][1]) + " * " + str(arr[2][2]) + " + " + str(arr[0][1]) + " * " + str(arr[1][2]) + " * " + str(arr[2][0]) + " + " + str(arr[0][2]) + " * " + str(arr[1][0]) + " * " + str(arr[2][1]) + ") - (" + str(arr[0][2]) + " * " + str(arr[1][1]) + " * " + str(arr[2][0]) + " + " + str(arr[0][1]) + " * " + str(arr[1][0]) + " * " + str(arr[2][2]) + " + " + str(arr[0][0]) + " * " + str(arr[1][2]) + " * " + str(arr[2][1]) + ") = " + str((arr[0][0] * arr[1][1] * arr[2][2] + arr[0][1] * arr[1][2] * arr[2][0] + arr[0][2] * arr[1][0] * arr[2][1]) - (arr[0][2] * arr[1][1] * arr[2][0] + arr[0][1] * arr[1][0] * arr[2][2] + arr[0][0] * arr[1][2] * arr[2][1]))
    
    if rowlong == 4:
        long = [0, 0, 0, 0, 0, 0, 0, 0] # los primeros 4 items son las lineas y los otros las columnas
        for i in range(4):
            long[i] = arr[i].count(0)
        for i in range(4, 8):
            subarr = [arr[0][i-4], arr[1][i-4], arr[2][i-4], arr[3][i-4]]
            long[i] = subarr.count(0)
        
        idx = long.index(max(long)) # para encontrar la linea o columna que mas 0 tiene para hacer menos operaciones
        
        mtx = []
        mtx2 = []
        arrn = []
        
        if idx < 4: # en caso de ser una fila la que mas 
            y = idx
            for x in range(4):
                n = arr[y][x]
                det = [] #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                
                for i in range(4):
                    if i != y:
                        linea = []
                        for a in range(4):
                            if a != x:
                                linea.append(arr[i][a])
                        det.append(linea)

                y2 = y + 1
                x2 = x + 1
                if n != 0:
                    res += f"{n}*(-1)^({y2}+{x2})*|{det[0]}, {det[1]}, {det[2]}|"
                else:
                    res += "0"
                if x != 3:
                    res += " + "
                
                mtx.append(det)
                arrn.append(n*((-1)**(y2+x2)))
                
            res += " = "
            
        else: # en caso de ser una columna
            x = idx-4
            for y in range(4):
                n = arr[y][x]
                det = [] #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                
                for i in range(4):
                    if i != y:
                        linea = []
                        for a in range(4):
                            if a != x:
                                linea.append(arr[i][a])
                        det.append(linea)

                y2 = y + 1
                x2 = x + 1
                if n != 0:
                    res += f"{n}*(-1)^({y2}+{x2})*|{det[0]}, {det[1]}, {det[2]}|"
                else:
                    res += "0"
                if x != 3:
                    res += " + "
                
                mtx.append(det)
                arrn.append(n*((-1)**(y2+x2)))
                
            res += " = "
        
        for i in mtx:
            mtx2.append(determinante(3, i))
            
        for i in range(4):
            if arrn[i] != 0:
                sarrus = "((" + str(mtx[i][0][0]) + " * " + str(mtx[i][1][1]) + " * " + str(mtx[i][2][2]) + " + " + str(mtx[i][0][1]) + " * " + str(mtx[i][1][2]) + " * " + str(mtx[i][2][0]) + " + " + str(mtx[i][0][2]) + " * " + str(mtx[i][1][0]) + " * " + str(mtx[i][2][1]) + ") - (" + str(mtx[i][0][2]) + " * " + str(mtx[i][1][1]) + " * " + str(mtx[i][2][0]) + " + " + str(mtx[i][0][1]) + " * " + str(mtx[i][1][0]) + " * " + str(mtx[i][2][2]) + " + " + str(mtx[i][0][0]) + " * " + str(mtx[i][1][2]) + " * " + str(mtx[i][2][1]) + "))"
                res += f"{arrn[i]}*{sarrus}"
            if i != 3 and arrn[i+1] > 0:
                res += " + "
        
        res += " = " + str(arrn[0]*mtx2[0]+arrn[1]*mtx2[1]+arrn[2]*mtx2[2]+arrn[3]*mtx2[3])
        
    if rowlong == 5:
        pass
    
    print(res)
    pyperclip.copy(res)
    return int(list(res.split())[-1])

while True:
    option = input("Opcion (determinante/d, rango/r): ").lower()
    arr = []
    arr.append(list(map(int, input().split())))
    rowlong = len(arr[0])
    for i in range(rowlong-1):
        arr.append(list(map(int, input().split())))
    
    if option == "determinante" or option == "d":
        res = determinante(rowlong, arr)
            
    elif option == "rango" or option == "r" or option == "heina":
        pass
    
