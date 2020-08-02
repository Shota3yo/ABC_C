from itertools import chain

n, m = map(int, input().split())
H = list(map(int, input().split()))

ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))

count = 0
skipset = []

for i in range(1, n+1):
    if i in skipset:
        continue
    f = {i}
    c= []
    e= []
    for j in ab:
        if i in j:
            c.append(j)
    d =set(chain.from_iterable(c)) -f
    #print(d)

    for k in d:
        e.append(H[k-1])

    if len(e)==0:
        count += 1
        #print('Yes')

        continue
    elif max(e) < H[i-1]:
        #print(i, H[i - 1], max(e))
        skipset.append(d)
        count += 1
        #print('Yes')
    else:

        pass

print(count)