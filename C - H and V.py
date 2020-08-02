import sys, copy
input = sys.stdin.readline
def main():
    h, w , k = map(int, input().split())
    ls = []
    for _ in range(h):
        ms = []
        t=str(input().rstrip())
        for i in range(len(t)):
            if t[i] =='.':
                ms.append(0)
            else:
                ms.append(1)
        ls.append(ms)

    def num(x, y):
        lt = copy.deepcopy(ls)
        x2 = format(x, 'b').rjust(h, '0')
        y2 = format(y, 'b').rjust(w, '0')
        for i in range(len(x2)):
            if x2[i]=='0':
                lt[i]= [0]*len(y2)
        for j in range(len(y2)):
            if y2[j]=='0':
                for t in range(len(x2)):
                    lt[t][j]= 0
        re = 0
        for i in lt:
            re += sum(i)
        return re
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            if num(i,j) == k:
                ans +=1
    print(ans)
if __name__ == '__main__':
    main()