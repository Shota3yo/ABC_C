import math

a, b, h, m = map(int, input().split())

jihun = 60*h + m


kakua= 2* math.pi * jihun/720
kakub =2* math.pi * m/60



ax = a * math.cos(kakua)
ay = a * math.sin(kakua)



bx = b * math.cos(kakub)
by = b * math.sin(kakub)


ans = math.sqrt((ax-bx)**2 + (ay-by)**2)

print(ans)