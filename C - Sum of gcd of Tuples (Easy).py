K = int(input())

ans = 0

import math

for i in range(1, K+1):
    for j in range(1, K+1):
        s=math.gcd(i, j)
        for k in range(1, K+1):
            ans += math.gcd(k, s)

print(ans)