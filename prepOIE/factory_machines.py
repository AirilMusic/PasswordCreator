# https://cses.fi/problemset/task/1620/
n, t = map(int, input().split())
arr = list(int(x) for x in input().split())
arr.sort()
l = len(arr)
times = [0]*l

if l > 1:
    while t > 0:
        times[0] += 1
        t -= 1
        for a in range(l-1):
            if times[a]*arr[a] > (times[a+1]+1)*arr[a+1]:
                times[a] -= 1
                times[a+1] += 1

    o = 0
    for i in range(l):
        v = arr[i]*times[i]
        if o < v:
            o = v
    print(o)
    
else:
    if t%arr[0] != 0:
        print(int(t/arr[0])+1)
    else:
        print(t/arr[0])
