# https://www.hackerrank.com/contests/oifem-iii-clasificatorio-fase-2/challenges/los-libros-de-julia/submissions/code/1356748586

k = int(input())
c = list(input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

pos = list(map(lambda x: [x], c))
pos2 = []

s = sum(arr)
for x in range(s-1):
    for a in range(len(pos)):
        for i in range(k):
            if pos[a][-1] == c[i]:
                if pos[a].count(c[i]) < arr[i]:
                    pos3 = list(reversed(pos[a]))
                    finished = False
                    count = 0
                    for u in pos3:
                        if u != c[i]:
                            break
                        else:
                            count += 1
                    if count < brr[i]-1:
                        pos3 = list(pos[a])
                        pos3.append(c[i])
                        pos2.append(pos3)
        
            else:
                if pos[a].count(c[i]) < arr[i]: 
                    pos3 = list(pos[a])
                    pos3.append(c[i])
                    pos2.append(pos3)

    pos = pos2
    pos2 = []

blacklist = []
for i in range(len(pos)):
    if len(pos[i]) == s and pos[i] not in blacklist:
        o = ""
        for a in pos[i]:
            o += a
            o += " "
        print(o.strip())
        blacklist.append(pos[i])
