# https://www.aceptaelreto.com/problem/statement.php?id=590

while True:
    t, n = map(int, input().split())
    if t == 0 and n == 0:
        break
    
    arr = sorted(list(map(int, input().split())))
    l = len(arr)
    
    if sum(arr) > 0 and sum(arr) > n:
        s = 0
        i0 = 0
        i1 = l-1
        for i in range(l):
            if s >= n:
                break
            else:
                found = False
                for a in range(i1-i0):
                    if s + arr[a] <= n:
                        s += arr[a]
                        i1 -= 1
                        found = True
                if found == False:
                    s += arr[0]
                    i0 += 1
                        
        
        print(s)
    
    elif sum(arr) == n:
        print(sum(arr))
    else:
        print("IMPOSIBLE")
