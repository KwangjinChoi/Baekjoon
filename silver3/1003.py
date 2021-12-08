import sys
T = int(input())
dp = [[1,0], [0,1]] + [[0,0]] * 39
for i in range(2, len(dp)):
    dp[i] = [x+y for x, y in zip(dp[i-1], dp[i-2])]
for _ in range(T):
    num = int(sys.stdin.readline())
    print(' '.join([str(i) for i in dp[num]]))
