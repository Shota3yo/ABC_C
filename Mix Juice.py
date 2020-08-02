n, k = map(int, input().split())
p = list(map(int, input().split()))

q= sorted(p)

import numpy as np

r= np.cumsum(q)

print(r[k-1])

