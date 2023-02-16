# https://jutge.org/problems/P11914_en/statement

while True:
    n = int(input())
    c = 0
    
    while n > 2:
        c += 1
        n /= 2

    print(c)
