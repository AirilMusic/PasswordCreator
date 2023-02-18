# https://www.hackerrank.com/contests/oifem-iii-clasificatorio-fase-2/challenges/cuadrados-blancos-2/submissions/code/1356575317

n = int(input())
tablero = []

for i in range(n):
    l = list(input())
    for a in l:
        tablero.append(a)

if "N" in set(tablero):
    print("NO")
else:
    print("SI")
