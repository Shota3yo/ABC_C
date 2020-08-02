n, m = map(int, input().split())
ans = ['t'] * n

for _ in range(m):
    s, c = map(int, input().split())
    if ans[s-1] =='t' or ans[s-1] == str(c):
        ans[s-1]= str(c)
    else:
        print(-1)
        exit(0)
if ans[0] == 't' and n >1:
    ans[0]=str(1)

ans = ''.join(ans).replace('t', str(0))
ans = int(ans)
l = str(ans)
if len(l) != n:
    print(-1)
else:
    print(ans)



