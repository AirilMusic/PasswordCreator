for x in range(int(input())):
    f, a, n = map(int, input().split())
    mi = a-1
    
    if a > 1:
        aula = []
        for i in range(f):
            if (i + 1) % 2 != 0:
                aula.append([j for j in range((i*a)+1, (i+1)*a+1)])
            else:
                aula.append([j for j in range((i+1)*a, i*a, -1)])

        for i in aula:
            if n in set(i):
                y = i.index(n)
                if y == 0:
                    print("VENTANA")
                elif y == mi:
                    print("PASILLO")
                else:
                    print(":(")
                
    elif a == 1:
        print("AMBOS")
    else:
        print(":(")