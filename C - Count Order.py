n= int(input())
import sys
pn = list(map(int, sys.stdin.readline().split()))
qn = list(map(int, sys.stdin.readline().split()))

a = 0
b= 0
m = [1]*(n+1)
m[0]=0

import math

for i in pn:

    if sum(m)==2:
        a += sum(m[:i]) +1
        break
    m[i] = 0

    a += sum(m[:i])* math.factorial(sum(m))


m = [1]*(n+1)
m[0]=0

for i in qn:

    if sum(m)==2:
        b += sum(m[:i]) +1
        break
    m[i] = 0

    b += sum(m[:i])* math.factorial(sum(m))


print(abs(a-b))



