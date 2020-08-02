import sys

n = int(input())
an = list(map(int, sys.stdin.readline().rstrip().split()))
bn = sorted(an, reverse=True)

count=1
if bn[-1]==bn[-2]:
    count=0
#print(bn)

for i in range(n-1):
    count += 1
    for j in range(i+1, n):
#        print(i, j)

        if bn[i]%bn[j]==0:
#            print('No')

            count -= 1

            break
#    print('ok', count)

print(count)