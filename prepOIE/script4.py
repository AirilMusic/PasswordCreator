for x in range(int(input())):
    n = int(input())
    p = int(n/2)
    intervalo = [0, n]
    while True:
        print(("? " + str(p)), flush = True)
        res = input()
        if res == "=":
            print(("! " + str(p)), flush = True)
            break
        elif res == "<":
            intervalo = [p+1, n]
            p = int(((intervalo[1]-intervalo[0])/2) + intervalo[0])
        else:
            intervalo = [intervalo[0], p-1]
            p = int(((intervalo[1]-intervalo[0])/2) + intervalo[0])
    r = input()
    if r == "-":
        break