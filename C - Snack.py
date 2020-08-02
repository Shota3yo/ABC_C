a, b = map(int, input().split())

import math

ans = a*b/math.gcd(a,b)
print(int(ans))