n, m = map(int, input().split())
ls1 = [[] for i in range(n+1)]
print(ls1)
for _ in range(m):
    a, b = map(int, input().split())
    print(a, b, ls1[a], ls1[b])
    ls1[a].append(b)
    ls1[b].append(a)
    print(a, b, ls1[a], ls1[b])
print(ls1)
