casos = int(input())
if 2000 < casos:
    casos = 2000
res = []
    
for caso in range(casos):
    n = int(input())
    c = [0] * (n+1)
    c[0] = 1
    
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            c[j] += c[j-i]
    
    res.append(c[n]) # funciona malllll aaaaaaaaaaaa :(

for i in res:
    print(i)
