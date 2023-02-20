# https://jutge.org/problems/P64493_en

while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr.remove(arr[0])
    
    min_diff = float('inf')
    for i in range(1 << n):
        sum1, sum2 = 0, 0
        for a in range(n):
            if i & (1 << a):
                sum1 += arr[a]
            else:
                sum2 += arr[a]
        diff = abs(sum1 - sum2)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)
