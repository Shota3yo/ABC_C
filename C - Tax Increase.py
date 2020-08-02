a, b = map(int, input().split())
x=10*b

import math
for i in range(10):
    if math.floor((x+i)*0.08)==a:
        print(x+i)
        exit(0)

print(-1)