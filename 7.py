from math import sqrt

def isPrime(n):
    for i in range(int(sqrt(n))+1, 1, -1):
        if n%i == 0:
            return False
    return True

cnt = 0
i=1
while(cnt != 10000):
    i +=1
    if isPrime(i):
        cnt += 1

print i
