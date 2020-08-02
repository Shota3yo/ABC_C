n = str(input())
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = int(n[3])

def m(x):
    re = a
    ls = [str(a)]
    for i in range(3):
        if (x>>i)&1 == 1 :
            re +=int(n[i+1])
            ls.append('+'+n[i+1])
        else:
            re -=int(n[i+1])
            ls.append('-'+n[i+1])
    return re, ls

for j in range(8):
    if m(j)[0]==7:
        print(''.join(m(j)[1])+'=7')
        exit()

