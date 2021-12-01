import sys
N = int(input())
cnt = N
for _ in range(N):
    string = sys.stdin.readline().split()[0]
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            continue
        elif string[i] in string[i+1:]:
            cnt -= 1
            break
print(cnt)