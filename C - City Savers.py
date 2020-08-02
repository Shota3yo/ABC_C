n = int(input())
a =list(map(int, input().split()))
b =list(map(int, input().split()))
ans = 0
for i in range(n):
    amari =max(b[i]-a[i], 0)
    ans += min(b[i], a[i]+a[i+1])
    a[i+1] = max(0, -amari+a[i+1])
print(ans)
