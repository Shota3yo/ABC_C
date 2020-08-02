n= int(input())
xn= list(map(int, input().split()))

t= n* 10000

for i in range(1, 101):
    a = sum([(j-i)**2 for j in xn])

    if t > a:
        t=a


print(t)