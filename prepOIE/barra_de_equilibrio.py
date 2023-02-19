# https://jutge.org/problems/P18679_en

m, n = map(int, input().split())
arr = list(map(int, input().split()))
pos = [0]

for i in range(n):
    pos2 = []
    for a in pos:
        if a + arr[i] <= m:
            pos2.append(a + arr[i])
        if a - arr[i] >= -m:
            pos2.append(a - arr[i])
    pos = pos2

for p in pos:
    print(p)
