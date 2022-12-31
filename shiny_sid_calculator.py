while True:
    pid0 = input("Pokemon ID (PID): ")
    pid=bin(int(pid0, 16))
    n00 = 0
    pid1 = ""
    for i in pid:
        if n00 > 1:
            pid1 += i
        n00 += 1
    while len(pid1)/2 < 16 or len(pid1)%2 != 0:
        pid1 = "0" + pid1
    
    tid0 = int(input("Trainer ID: "))   
    tid=str(bin(tid0))
    n000 = 0
    tid1 = []
    for i in tid:
        if n000 > 1:
            tid1.append(i)
        n000 += 1
    if len(tid1) < 16:
        zn = 16 - len(tid1)
        for i in range(zn):
            tid1.insert(0, "0")
    
    hid=[]
    lid=[]
    
    sid=[]

    n0 = 0 
    for i in pid1:
        if n0 < int(len(pid1)/2):
            hid.append(i)
        else:
            lid.append(i)
        n0 += 1
    
    for i in range(len(lid)):
        if (int(hid[i])+int(lid[i])+int(tid1[i]))%2 != 0:
            sid.append("1")
        else:
            sid.append("0")
    
    sid = int(''.join(sid), 2)
    print("Shiny SID for pokemon with", pid0, "PID and", tid0, "TID:", sid, "\n\n\n\n\n")
