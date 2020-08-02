a, b, n = map(int, input().split())
from decimal import Decimal


y = [(a*i)//b-a*(i//b) for i in range(1, n+1)]
ans = max(y)
print(ans)