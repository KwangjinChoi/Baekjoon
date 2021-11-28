import sys
T = int(input())
answer = 1
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split(' '))
    if x == answer:
        answer = y
    elif y == answer:
        answer = x
print(answer)
