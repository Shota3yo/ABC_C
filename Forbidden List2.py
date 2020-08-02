import sys

x, n = map(int, input().split())
pn = list(map(int, sys.stdin.readline().rstrip().split()))

if x not in pn:
    print(x)
    exit(0)

for i in range(1,100):
    if x-i not in pn:
        print(x-i)
        exit(0)
    elif x+i not in pn:
        print(x + i)
        exit(0)
