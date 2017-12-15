from math import sqrt

def isPrime(n):
    for i in range(n-1, 1, -1):
        if n%i == 0:
            return False
    return True

num = 600851475143

n = int(sqrt(num))+1
print num

for i in range(2, n):
    if num%i == 0 and isPrime(i):
        print i
        num = num/i
        if num == 1:
            break

