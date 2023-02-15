for x in range(int(input())):
    a, b, k = list(input().split())
    n = int(a, int(k)) + int(b, int(k))
    n2 = []
    if n == 0:
        print(0)
    else:    
        while n > 0:
            n2.insert(0, str(n % int(k)))
            n = n // int(k)

        res = "".join(n2)
        print(res)
