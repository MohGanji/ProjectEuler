from math import sqrt

primes = [2]
def isPrime(n):
    for i in primes:
        if i > int(sqrt(n)):
            return True
        if n%i == 0:
            return False
    return True

sm = 2
for i in range(3, 2*10**6):
    if isPrime(i):
        sm += i
        primes.append(i)

print sm
