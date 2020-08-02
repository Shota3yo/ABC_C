n = int(input())
import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def f(x):
    c = collections.Counter(prime_factorize(x))
    d = c.values()
    ans = 1
    for i in d:
        ans *= i+1
    return ans
sumu =0
for i in range(1, n+1):
    sumu += i * f(i)
print(sumu)

