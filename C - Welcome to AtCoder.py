n, m = map(int, input().split())

co = 0
pe = 0

ac= [0] * (n+1)
wa= [0] * (n+1)

for _ in range(m):
    p, s = map(str, input().split())
    p = int(p)
    if ac[p]==0 and s == 'AC':
        co += 1
        ac[p] =1
        if wa[p]>0:
            pe += wa[p]
    elif ac[p] == 0 and s == 'WA':
        wa[p] += 1

print('{} {}'.format(co, pe))

