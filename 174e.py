n, k = map(int, input().split())
an = list(map(int, input().split()))

maxi = max(an)
if k == 0:
    print(maxi)
    exit(0)


def judge(t):
    m = 0
    for i in an:
        if i%t == 0:
            m +=i//t
        else:
            m += i//t+1
    #print('judge', m, n+k)
    if m <= n+k:
        #print("true")
        return True
    else:
        #print("false")
        return False

mini = 0
#maxi = max(an)

while mini+1 != maxi:
    check = (mini+maxi)//2
    #print(check)
    if judge(check):
        maxi = check
        #print(mini, maxi)
    else:
        mini = check
        #print(mini, maxi)

print(maxi)