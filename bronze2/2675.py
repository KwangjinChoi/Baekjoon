import sys
T = int(input())

for _ in range(T):
    res = ''
    cnt, str = sys.stdin.readline().split()
    for c in str:
        res += c*int(cnt)
    print(res)