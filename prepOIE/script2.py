for x in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    c = 0
    while arr[0] > arr[-1]:
        while arr[0] > arr[-1]:
            arr[0] = int(arr[0]/2)
            c += 1
        arr.sort(reverse=True)
    
    print(c)