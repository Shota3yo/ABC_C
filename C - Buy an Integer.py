a,b,x = map(int, input().split())


def d(n):
    return len(str(n))

t = True
ans =1
while ans <= 10*9:
    if x >= a*ans + b* d(ans):
        ans += 1
    elif x < a*ans + b* d(ans):
        print(ans-1)
        exit(0)
