from decimal import Decimal


a, b = input().split()
a= Decimal(a)
b= Decimal(b)

c = a*b

print(int(c))
