n= int(input())

factors=[]

for i in range(2, int(n**(0.5))+2):
    if n%i == 0:
        cnt=0
        while n%i==0:
            cnt+=1
            n //=i
        factors.append([i,cnt])
if n!=1:
    factors.append([n, 1])

print(factors)
