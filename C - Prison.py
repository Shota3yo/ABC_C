n, m = map(int, input().split())

card = [0]*(n+2)
for _ in range(m):
    l, r = map(int, input().split())
    card[l] +=1
    card[r+1] -=1

import numpy as np
card = list(np.cumsum(card))
print(card.count(m))

