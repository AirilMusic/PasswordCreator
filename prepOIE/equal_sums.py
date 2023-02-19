# https://jutge.org/problems/P11655_en

from itertools import combinations

s = int(input())
n = int(input())
arr = list(map(int, input().split()))
o = []

for i in range(n+1):
    conv = combinations(arr, i)
    
    for a in conv:
        if sum(a) == s:
            o.append(a)

o = list(set(o))

for i in o:
    print(i)
