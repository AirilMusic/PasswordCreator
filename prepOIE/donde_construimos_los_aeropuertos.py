# NO FUNCA BIEN
inp = ""
res = []

while inp != "0 0":
    inp = input()
    if inp != "0 0":
        n, m = [int(x) for x in list(inp.split())] #n = numero de localidades, m = numero de autopistas
        c = list(map(int, input().split())) #costes un aeropuerto en cada localidad [i]
        a = [] #autopistas, [X,Y,C] --> X, Y son las dos localidades (nodos) y C es el costo de la carretera entre ellas
        for i in range(m):
            a.append(list(map(int, input().split())))

        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        aeropuertos = sum([1 for i in c if i < float('inf')])

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                elif rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                else:
                    parent[rooty] = rootx
                    rank[rootx] += 1

        coste = 0
        a.sort(key=lambda x: x[2])
        for i in range(m):
            x, y, z = a[i]
            x, y = x-1, y-1
            if find(x) != find(y):
                coste += z
                aeropuertos -= 1
                union(x, y)
                if aeropuertos == 1:
                    break

        coste += sum([c[i] for i in range(n) if c[i] < float('inf')])
        res.append(str(coste) + " " + str(aeropuertos))

for i in res:
    print(i)