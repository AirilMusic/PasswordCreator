# https://jutge.org/problems/P78497_es/statement

from math import sqrt

while True:
    try:
        a, b, c, d, n = map(int, input().split())

        p = (3*a*c - b**2)/(3*a**2)
        q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)
        delta = (q/2)**2 + (p/3)**3
        
        u = (-q/2 + sqrt(delta))**(1/3) if delta >= 0 else (-q/2 + complex(delta).sqrt())**(1/3)
        v = (-q/2 - sqrt(delta))**(1/3) if delta >= 0 else (-q/2 - complex(delta).sqrt())**(1/3)
        x = u + v - b/(3*a)

        if x.imag == 0 and 0 < x.real <= n:
            s = int(x.real)
        else:
            x = x.real
            s = round(x)
            while s > 0 and (a*s**3 + b*s**2 + c*s - d) > 0:
                s -= 1
            while (a*s**3 + b*s**2 + c*s - d) < 0:
                s += 1
                
        print(s)

    except:
        break
