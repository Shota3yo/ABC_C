n, m, k = map(int, input().split())
an= list(map(int, input().split()))
bm= list(map(int, input().split()))
an.insert(0,0)
bm.insert(0,0)
ans = 0
import numpy as np
cn = np.cumsum(an)
for i in range(n+1):
    x=cn[i]
    if k <x:
        break
    for j in range(m+1):
        x += bm[j]
        if k >= x and i+j > ans:
            ans = i+j
        elif k <x:
            break
print(ans)

