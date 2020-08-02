x, y = map(int, input().split())

for i in range(x+1):
    if y== 2*i + 4*(x-i):
        print('Yes')
        exit(0)
print('No')