import sys
N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list = sorted(num_list)
for num in num_list:
    print(num)