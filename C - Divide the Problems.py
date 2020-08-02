n = int(input())
d =list(map(int, input().split()))
d.sort()
s = int(n/2)
ans = d[s] - d[s-1]
print(ans)


