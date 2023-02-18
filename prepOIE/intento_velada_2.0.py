for x in range(int(input())):
    m1, m2, m3 = map(int, input().split())
    t = m1 + m2 + m3
    t1 = t
    n1 = 0
    n2 = 0
    n3 = 0
    
    if t1/10 >= 1:
        n1 = int(t1/10)
        t1 -= (n1*10)
    if t1%5 == 0:
        n2 = int(t1/5)
        t1 -= (n2*5)
    if t1%3 == 0:
        n3 = int(t1/3)
        t1 -= (n3*3)

    if t1 == 0:
        print(n1, n2, n3) ######################## HASTA AQUI TODO BIEN, CREO #######################
    else:
        if t%5 == 0:
            print(0, 1, 0)
        else:
            n1 = 0
            n2 = 0
            n3 = 0
            found = False
            tn = int(t/10)
            for i in range(tn+1):
                t1 = t
                if (t-(10*i))/10 >= 1:
                    n1 = int((t-(10*i))/10)
                    t1 = t-(n1*10)
                if t1%5 == 0:
                    n2 = 1
                    print(n1, n2, n3)
                    found = True
                    break
                else:
                    tn1 = int(t/5)
                    if tn1 == 0:
                        tn1 += 1
                    for a in range(tn1):
                        t2 = t1
                        if (t2-(5*a))/5 >= 1:
                            n2 = int((t2-(5*a))/5)
                            t2 -= n2*5
                        n3 = 0
                        if t2%3 == 0:
                            found = True
                            n3 = int(t2/3)
                            break
                if found:
                    if n1 > 0:
                        n1 -= 1
                    if n2 >0:
                        n2 -= 1
                    print(n1, n2, n3)
                    break
            if found == False:        
                if t%3 == 0:
                    print(0, 0, int(t/3))
                else:
                    print(-1, -1, -1)
