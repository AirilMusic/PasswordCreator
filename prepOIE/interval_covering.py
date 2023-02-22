# https://jutge.org/problems/P37902_en/

while True:
    try:
        arr = list(input().split())
        n = int(arr[0])
        arr.remove(arr[0])
        arr.sort()
        
        n1 = float(arr[0])
        n2 = float(arr[1])
        idx = 1
        for i in range(n-1):
            print("n1:", n1, "n2:", n2, "idx:", idx, "arri:", float(arr[i]), "arri1:", float(arr[i+1]))
            if float(arr[i]) < float(arr[i+1]):
                if n1 < n2:
                    if float(arr[i+1])-float(arr[i]) < n2-n1:
                        idx = i + 1
                        n1 = float(arr[i])
                        n2 = float(arr[i+1])
                else:
                    if float(arr[i+1])-float(arr[i]) < n1-n2:
                        idx = i + 1
                        n1 = float(arr[i])
                        n2 = float(arr[i+1])
            else:
                if n1 < n2:
                    if float(arr[i])-float(arr[i+1]) < n2-n1:
                        idx = i + 1
                        n1 = float(arr[i])
                        n2 = float(arr[i+1])
                else:
                    if float(arr[i])-float(arr[i+1]) < n1-n2:
                        idx = i + 1
                        n1 = float(arr[i])
                        n2 = float(arr[i+1])
        print(idx)
    except:
        break
