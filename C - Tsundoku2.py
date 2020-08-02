n, m, k = map(int, input().split())
from collections import deque
a= deque(map(int, input().split()))
b= deque(map(int, input().split()))
ans =0

while k >=0 and len(a) + len(b) >=1:
    if len(a)>0 and len(b)>0:
        if a[0] >= b[0]:
            k -= b.popleft()
            if k >= 0:
                ans += 1
        else:
            k -= a.popleft()
            if k >= 0:
                ans += 1
    elif len(a) == 0 and len(b) > 0:
        k -= b.popleft()
        if k >= 0:
            ans += 1
    elif len(b) == 0 and len(a) > 0:
        k -= a.popleft()
        if k >= 0:
            ans += 1
print(ans)
