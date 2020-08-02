n = int(input())

m= int(n**0.5)

while m >= 1:
    if n%m ==0:
        print(int(n/m)+m-2)
        exit(0)
    else:
        m -=1
