# ya estoy cansadita asi que no es raro que empiece a decir tonterias
# cual es la operación matemática que mejor se les da a las amebas? las divisiones :)

inp = ""
res = []

while inp != "0 0":
    inp = input()
    if inp != "0 0":
        n, d = list(inp.split()) #n = parcelas, d = dias
        a = list(input().split()) # amebas por cada celda
        a2 = []
        for i in range(len(a)):
            a2.append(0)
            
        for u in range(int(d)):
            for i in range(len(a)):
                if a[i] != 0:
                    n = 0
                    n2 = 0
                    if i - 1 < 0:
                        n = len(a)-1
                    else:
                        n = i - 1
                    if len(a)-1 < i + 1:
                        n2 = 0
                    else:
                        n2 = i +1
                        
                    if a2[n] == 0:
                        a2[n] = a[i]
                    else:
                        a2[n] += a[i]
                    if a[n] == 0:
                        a[n] = a[i]
                    else:
                        a[n] += a[i]
            a = a2
        c = []
        for i in a:
            if i != 0:
                c.append(i)
        res.append(c)
        
for i in range(len(res)):
    s = ""
    for e in res[i]:
        s += str(int(e)%((10**9)+7)) + " "
    print(s)