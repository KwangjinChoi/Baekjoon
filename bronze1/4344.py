import sys

C = int(input())
for _ in range(C):
    score_list = list(map(int,sys.stdin.readline().split()))
    mean = sum(score_list[1:])/score_list[0]
    cnt = 0
    for score in score_list[1:]:
        if mean < score:
            cnt += 1
    res = cnt/score_list[0]*100
    print(f'{res:.3f}%')