import sys
input = sys.stdin.readline
def main():
    n = int(input())
    an = list(map(int, input().split()))
    an.sort(reverse=True)
    ans = 0
    for i in range(1, n):
        d=i//2
        ans +=an[d]
    print(ans)
if __name__ == '__main__':
    main()