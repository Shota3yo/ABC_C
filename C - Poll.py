n = int(input())

dic = {}
for _ in range(n):

    s =input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s]=1

maxdic = max(dic.values())

ans = [i for i in dic if dic[i]==maxdic]
print('\n'.join(sorted(ans)))


