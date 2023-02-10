inp = ""
arrs = []

while inp != "0":
    inp = input()
    if inp != "0":
        arrs.append(inp.split()) 
        
for i in range(len(arrs)):
    n = int(arrs[i][0])
    p = int(arrs[i][1])
    q = int(arrs[i][2])
    
    l = [] #lista de numeros que cumplen con los requisitos
    
    for e in range(1, n + 1):
        is_divisible = False
        for i in range(2, int(e**0.5) + 1):
            if e % i == 0 and i not in (p, q):
                is_divisible = True
                break
        if not is_divisible:
            if e % p == 0 and e % q == 0:
                l.append(e)

    if l != []:
        print(max(l))
    else:
        print(0)