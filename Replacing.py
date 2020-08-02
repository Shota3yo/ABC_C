import sys
n = int(input())
an = list(map(int, sys.stdin.readline().rstrip().split()))
q = int(input())

import numpy as np
from collections import deque
import collections

li = np.zeros(100001)
print(li)
for a in an:
    li[a] +=1


sum = np.sum(an)
ans = deque()




for _ in range(q):
    b,c = map(int, input().split())
    if li[b]:
        if b == i:

            sum += j*(c-b)
            print(new)

    print(new)


    ans.append(sum)

while ans:
    print(ans.popleft())



