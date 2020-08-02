n = int(input())
import sys
pn = list(map(int, sys.stdin.readline().split()))

ans = 1
mini = pn[0]

for i in range(1, n):
    mini = min(mini, pn[i])
    if mini==pn[i]:
        ans += 1

print(ans)