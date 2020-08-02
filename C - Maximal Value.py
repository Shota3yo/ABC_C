n = int(input())
bn =list(map(int, input().split()))

ans = bn[0] + bn[-1]

for i in range(1, n-1):
    ans += min(bn[i], bn[i-1])

print(ans)