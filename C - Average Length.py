n = int(input())
xyn = []
for _ in range(n):
    x, y = map(int, input().split())
    xyn.append([x,y])
import itertools
ls = list(itertools.permutations(range(1, n+1)))


leng=0

for i in ls:
    for j in range(len(i)-1):
        z=i[j]
        a=i[j+1]
        leng += ((xyn[z-1][0]-xyn[a-1][0])**2+(xyn[z-1][1]-xyn[a-1][1])**2)**0.5

ans = leng/len(ls)
print(ans)

