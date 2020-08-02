import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
an = list(map(int, sys.stdin.readline().rstrip().split()))


import numpy as np


t= min(k, 45)
from numba.decorators import jit

@jit
def imos(a, n):
    bn = [0]*n
    for i in range(n):
        bn[max(i - a[i], 0)] += 1

        if i+ a[i]+1 <n:
            bn[i+a[i]+1] -=1
    return np.cumsum(bn)


for k in range(t):
    an = imos(an, n)


print(*an)
