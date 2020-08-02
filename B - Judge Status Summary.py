n = int(input())
ans=[0]*4
for _ in range(n):
    s=str(input())
    if s == 'AC':
        ans[0] +=1
    elif s == 'WA':
        ans[1] += 1
    elif s == 'TLE':
        ans[2] += 1
    else:
        ans[3] += 1
print('AC x '+ str(ans[0]))
print('WA x '+ str(ans[1]))
print('TLE x '+ str(ans[2]))
print('RE x '+ str(ans[3]))


