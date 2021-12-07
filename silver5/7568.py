import sys
N = int(input())
w_h_list = []
for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    w_h_list.append((weight, height))
    
res = [1]*len(w_h_list)

for i in range(len(w_h_list)):
    for j in range(len(w_h_list)):
        if i == j:
            continue
        if w_h_list[i][0] < w_h_list[j][0] and w_h_list[i][1] < w_h_list[j][1]:
            res[i] += 1

print(' '.join(str(e) for e in res))