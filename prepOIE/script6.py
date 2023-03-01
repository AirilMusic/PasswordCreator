from math import gcd
MOD = 10**9 + 7

def count_permutations(n, cards):
    up = []
    down = []
    for i in range(n):
        a, b = cards[i]
        if gcd(a, b) == 1:
            up.append(a)
            down.append(b)
    m = len(up)
    if m == 0:
        return 0
    up_lcm = up[0]
    for i in range(1, m):
        up_lcm = up_lcm * up[i] // gcd(up_lcm, up[i])
    down_lcm = down[0]
    for i in range(1, m):
        down_lcm = down_lcm * down[i] // gcd(down_lcm, down[i])
    ans = pow(2, n-m, MOD)
    ans = ans * (pow(2, m, MOD) - pow(2, m-1, MOD)) % MOD
    ans = ans * pow(pow(2, m, MOD) - 1, MOD-2, MOD) % MOD
    ans = ans * pow(up_lcm, MOD-2, MOD) % MOD
    ans = ans * pow(down_lcm, MOD-2, MOD) % MOD
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    cards = [list(map(int, input().split())) for _ in range(n)]
    ans = count_permutations(n, cards)
    if ans >= (10**9) + 7:
        print(ans%(10**9)+7)
    else:
        print(ans)