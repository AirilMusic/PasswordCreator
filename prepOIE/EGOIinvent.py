# https://www.hackerrank.com/contests/oifem-iii-clasificatorio-fase-2/challenges/egoinvent/submissions/code/1356577866

n = int(input())
co = []

a = 0
b = 0
c = 0

for i in range(n):
    inp = list(map(int, input().split()))
    p = inp[0]
    ps = (inp[1] + inp[2] + inp[3] + inp[4] + inp[5] + inp[6])/6
    co.append([ps, p])

r = 0
for i in range(len(co)):
    id = list(str(co[i-r][1]))
    if int(id[len(id)-1]) != 0 and int(id[len(id)-1] != '5'):
        co.remove(co[i-r])
        r += 1
co.sort()
co.reverse()

l1 = len(co)

na = int((l1/100)*10)
nb = int((l1/100)*15)
nc = int((l1/100)*25)

r = 0
for i in range(na):
    if co[i-r][1] == 125:
        a += 1
    co.remove(co[i-r])
    r += 1

r = 0
for i in range(nb):
    if co[i-r][1] == 125:
        b += 1
    co.remove(co[i-r])
    r += 1

r = 0
for i in range(nc):
    if co[i-r][1] == 125:
        c += 1
    co.remove(co[i-r])
    r += 1

print(a)
print(b)
print(c)
