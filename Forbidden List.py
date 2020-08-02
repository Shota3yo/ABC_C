import sys

x, n = map(int, input().split())
pn = list(map(int, sys.stdin.readline().rstrip().split()))

qn = set([i for i in range(0,102)]) - set(pn)

qn = list(qn)

for i in range(102-n):
    if qn[i]==x:
        print(x)
        exit(0)
    elif x-qn[i+1]<0:
        if x-qn[i] <= qn[i+1]-x:
            print(qn[i])
            exit(0)
        else:
            print(qn[i+1])
            exit(0)
