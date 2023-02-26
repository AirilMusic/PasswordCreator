# cuantos numeros que son capicuas y primos, hay entre 1 y 1008002?

def isPrime(n):
    if n <= 1:
        return "Not prime"

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not prime"
    
    return "Prime"

c = 0
for i in range(1, 1008002):
    if list(str(i)) == list(reversed(str(i))) and isPrime(i) == "Prime":
        c += 1
        print(i)

print("\nHay", c, "numeros que son primos y capicuas al mismo tiempo\n")
