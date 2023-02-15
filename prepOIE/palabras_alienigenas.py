for x in range(int(input())):
    arr = sorted(list(input()))
    chars = list("abcdefghijklmnopqrstvwxyz")
    c = [0]*len(chars)
    for i in set(arr):
        for a in range(len(chars)):
            if chars[a] == i:
                c[a] = (arr.count(i))

    flag = True
    for i in range(len(c)-1):
        if c[i] < c[i+1]:
            flag = False
            break
            
    if flag:
        print("SIGUE LA REGLA")
    else:
        print("NO SIGUE LA REGLA")
