k = int(input())

m = 0

for i in range(1, 10**7):
    n = m *10 +7
    m = n % k
    if m == 0:
        print(i)
        exit(0)

print(-1)