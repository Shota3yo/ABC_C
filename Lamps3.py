import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
an = list(map(int, sys.stdin.readline().rstrip().split()))

import numpy as np

t= min(k, 45)

for _ in range(t):
    bn = [0]*n
    for i in range(n):
        bn[max(i - an[i], 0)] += 1

        if i+ an[i]+1 <n:
            bn[i+an[i]+1] -=1
    an = np.cumsum(bn)


print(*an)
