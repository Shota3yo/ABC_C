n = int(input())
hn =list(map(int, input().split()))

ans = 0
count = 0
for i in range(n-1):
    if hn[i+1] <= hn[i]:
        count += 1
    else:
        ans = max(ans, count)
        count=0

ans = max(ans, count)

print(ans)
