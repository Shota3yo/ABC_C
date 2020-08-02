n = int(input())
v =list(map(int, input().split()))
v.sort()
a = v[0]
for i in range(1, n):
    a = (a+v[i])/2
print(a)
