n, k = map(int, input().split())
an = list(map(int, input().split()))

import numpy as np

t= min(k, 45)
bn = np.zeros((t,n), dtype=int)

for k in range(t):
    if k==0:
        for i in range(n):
            for j in range(max(i - an[i], 0), min(n, i + an[i] + 1)):
                bn[k][j] += 1
    else:
        for i in range(n):
            for j in range(max(i - bn[k - 1][i], 0), min(n, i + bn[k - 1][i] + 1)):
                bn[k][j] += 1

print(*bn[t-1])