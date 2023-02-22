# https://www.hackerrank.com/contests/ijmszfeelfqrwqfeyiaz/challenges/problemas

while True:
    try:
        n, m = map(int, input().split())
        top = [] #topings
        arr = [] #cantidad de topings
        t = 0 #total de porciones
        
        for i in range(n):
            req = list(input().split())
            t += int(req[0])
            req.remove(req[0])
            items = list(set(req))
            for a in items:
                if a not in top:
                    top.append(a)
                    arr.append(0)
                c = req.count(a)
                arr[top.index(a)] += c

        if t%8 != 0:
            print("NO")
        else:
            if n > 1:
                posible = True
                for i in arr:
                    if int(i)%8 != 0:
                        posible = False
                        print("NO")
                        break
                if posible:
                    print("SI")
            else:
                print("SI")
                
    except:
        break
