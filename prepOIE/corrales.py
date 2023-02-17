for x in range(int(input())):
    n, a = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    l = len(arr)
    dp = [] #distancia de los corrales
    
    if a <= l-1:
        for i in range(l-1):
            dp.append(arr[i+1]-arr[i])
        dp.sort()
        print(dp[a-1])
        
    else:
        for i in range(l-1):
            for u in range(i+1, l):
                sdp = set(dp)
                rst = arr[u]-arr[i]
                if len(dp) < a and rst not in sdp:
                    dp.append(rst)
                else:
                    if rst not in sdp:
                        for v in range(len(dp)):
                            if dp[v] > rst:
                                dp[v] = rst
                                break
        dp.sort()
        print(dp[a-1])
