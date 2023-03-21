def next_move(posr, posc, board): #posr: 0 posc: 0 board: [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
    dpos = []
    for y in range(5):
        for x in range(5):
            if board[y][x] == "d":
                dpos.append([x, y])
    
    x = posc
    y = posr
    
    l = len(dpos)
    for _ in range(l):
        dis = [] #distancias del bot a la basura
        for i in range(len(dpos)):
            dx, dy = 0, 0
            if x <= dpos[i][0]:
                dx = dpos[i][0] - x
            else:
                dx = x - dpos[i][0]
            
            if y <= dpos[i][1]:
                dy = dpos[i][1] - y
            else:
                dy = y - dpos[i][1]
            
            dis.append(dx + dy)
            
        idx = dis.index(min(dis))
        d = dpos[idx]
        
        if y > d[1]:
            for i in range(y-d[1]):
                print("UP")
        else:
            for i in range(d[1]-y):
                print("DOWN")
        
        if x > d[0]:
            for i in range(x-d[0]):
                print("LEFT")
        else:
            for i in range(d[0]-x):
                print("RIGHT")
        
        x = d[0]
        y = d[1]
        
        print("CLEAN")
        dpos.remove(dpos[idx])
