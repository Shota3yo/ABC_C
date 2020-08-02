n = int(input())

def trans(t):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return alph[t]

ans = ''
i=n
while i > 0:
    s = (i-1) % 26
    i = (i-1) //26
    ans = trans(s) + ans

print(ans)