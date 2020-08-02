n = int(input())
a = list(map(int, input().split()))

b = sorted(a, reverse=True)


ans=1

if min(b) == 0:
    print(0)
    exit(0)

for i in range(n):
    ans *= b[i]
    if ans > 10 ** 18:
        print(-1)
        exit(0)



print(ans)