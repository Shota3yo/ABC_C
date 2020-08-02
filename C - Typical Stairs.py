n,m = map(int, input().split())

a = [1, 1]
for i in range(2, 10**5+4):
    u = a[i-1] + a[i-2]
    a.append(u)
print(a)


ans = 1
ls = [-1]
for _ in range(m):
    ls.append(int(input()))
ls.append(n+1)
ms = []
for i in range(m+1):
    t = ls[i+1]-ls[i]-2
    ms.append(t)
for j in ms:
    ans *= a[j]
ans = ans %1000000007
print(ans)