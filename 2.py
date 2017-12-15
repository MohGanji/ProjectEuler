def fib(a, b):
    return (b, a+b)

a = 1
b = 2
ans = 2
while (b < 4*10**6):
    a, b = fib(a, b)
    ans = ans + b if b%2 ==0 else ans

print ans
