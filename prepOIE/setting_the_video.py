while True:
    try:
        arr = list(input().split())
        n = int(arr[0])
        arr.remove(arr[0])

        ls = []
        c = 0
        for i in range(n):
            ls.append([int(arr[c]), int(arr[c+1])])
            c += 2
        ls.sort()

        t = ls[0]
        pb = []
        for i in range(1, n):
            if ls[i][0] == t[0] or ls[i][0] <= t[1]:
                pb.append(ls[i])
            else:
                t = ls[i]
        for i in pb:
            ls.remove(i)
        print(len(ls))
    except:
        break
