MOD = int(1e9) + 7

def solve(n, a):
    # Calcular el primer stack
    stack1 = []
    for i in range(n):
        while stack1 and a[stack1[-1]] >= a[i]:
            stack1.pop()
        if not stack1:
            stack1.append(i)
        else:
            # Guardar solo el índice del mínimo
            stack1.append(stack1[-1])
    # Calcular el segundo stack
    stack2 = []
    for i in reversed(range(n)):
        while stack2 and a[stack2[-1]] <= a[i]:
            stack2.pop()
        if not stack2:
            stack2.append(i)
        else:
            # Guardar solo el índice del máximo
            stack2.append(stack2[-1])
    # Calcular la respuesta final
    ans = 0
    for i in range(n):
        # Calcular la contribución de este índice
        left_min = a[stack1[i]]
        right_max = a[stack2[n - i - 1]]
        contrib = (left_min * right_max) % MOD
        ans = (ans + contrib) % MOD
    return ans

# Lectura de la entrada
T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)