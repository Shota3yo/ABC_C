h, m, i, n, k = map(int, input().split())

fun1 = 60 * h + m
fun2 = 60 * i + n

sa = fun2-fun1

if sa > k:
    ans = sa -k
else:
    ans = 0

print(ans)