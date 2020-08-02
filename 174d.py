n = int(input())
s = input()

w=0
for i in range(n):
    if s[i] == 'W':
        w += 1

ans = 0
for i in range(n-w):
    if s[i] =='W':
       ans += 1

print(ans)