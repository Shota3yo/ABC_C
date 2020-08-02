x = int(input())
import math

def sosu(x):
    for i in range(2, math.floor(x**0.5)):
        if x%i ==0:
            return True

    return False

while sosu(x):
    x +=1

print(x)

