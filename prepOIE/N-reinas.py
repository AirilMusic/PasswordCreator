# https://jutge.org/problems/P17921_en

n = int(input())

for i in range(1, n+1): # para que pruebe todas las posibilidades en la primera columna
    arr = [[i]]
    arr2 = []
    
    for j in range(1, n): #para ir columna a columna despues de la primera
        pb = [] # pa borrar XD
        for a in arr:
            blacklist = []
            for v in range(len(a)):
                blacklist.append(a[v])
                if a[v]+j-v <= n and a[v]+j-v not in set(blacklist): 
                    blacklist.append(a[v]+j-v)
                if a[v]-j+v >= 1 and a[v]-j+v not in set(blacklist): 
                    blacklist.append(a[v]-j+v)
            
            if len(set(blacklist)) >= n:
                pb.append(a)
            else:
                for v in range(1, n+1): #para ver en la columna en la que estamos que casillas son posibles
                    if v not in set(blacklist):
                        arr3 = list(a)
                        arr3.append(v)
                        arr2.append(arr3)
        for a in pb:
            arr.remove(a)
        arr = arr2
        arr2 = []
    for e in arr:
        if len(e) == n: # printearlo de forma grafica si es un caso posible
            g = [""]*n
            for x in range(n):
                for i in range(len(e)):
                    if e[i] != x+1:
                        g[x] += "."
                    else:
                        g[x] += "Q"
            for o in g:
                print(o)
            print("")
