res = []
for z in range(int(input())):
    n = int(input())
    ju = list(input().split())
    ju2 = set(ju)
    
    for m in range(int(input())):
        q = list(input().split())
        k = int(q[0])
        juego = q[1]
        
        if juego in ju2 and k <= ju.count(juego):
            for i in range(len(ju)):
                if ju[i] == juego:
                    if 1 < k:
                        k -= 1  
                    else:
                        res.append(i+1)
                        break
        else:
            res.append("NO JUEGA")
        
zero = input()

for i in res:
    print(i)