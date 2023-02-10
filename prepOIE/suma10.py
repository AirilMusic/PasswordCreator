arrs = []
res = []

for i in range(int(input())):
    arrs.append([input().split(),input().split()])
    s = int(arrs[i][0][0])
    n = int(arrs[i][0][1])
    a = [] 
    for u in arrs[i][1]:
        a.append(int(u))
        
    co = 0
    for u in range(int(n/2)):
        for e in range(len(a)-1):
            if a[u-co]+a[e+1-co] == 10:
                a.remove(a[u-co])
                a.remove(a[e-co])
                co += 1
                break
    
    if len(a) > 1:
        co = 0
        for u in range(int(len(a)/2)):
            for e in range(len(a)-1):
                if a[u-co] == a[e+1-co]:
                    a.remove(a[u-co])
                    a.remove(a[e-co])
                    co += 1
                    break
    
    if len(a) == 0:
        res.append("SE PUEDE, IZAN!")
    else:
        res.append("NO MERECE LA PENA :(")
        
for i in res:
    print(i)