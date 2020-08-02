h = int(input())
s =0
ans = 0
while h > 0:
    h = int(h/2)
    ans +=2**s
    s+=1
print(ans)
