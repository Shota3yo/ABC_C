n, k = map(int, input().split())

if n <= k :
    print(min(n, k-n))
    exit(0)
if n>k:
    n = n%k
    print(min(n, k-n))

