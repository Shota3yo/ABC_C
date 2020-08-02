n = int(input())
an=[]
for _ in range(n):
    an.append(int(input()))
bn = sorted(an, reverse=True)
s = bn[0]
t= bn[1]
for i in an:
    if i == s:
        print(t)
    else:
        print(s)

