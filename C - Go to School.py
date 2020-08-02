import sys
n= int(input())
an = list(map(int, sys.stdin.readline().split()))
ans = ['']*n
for i in range(n):
    ans[an[i]-1] = str(i+1)

print(' '.join(ans))
