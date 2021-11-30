m, d = map(int,input().split())
day = ['MON', 'TUE','WED','THU','FRI','SAT','SUN']
date_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
if m == 1:
    print(day[(d-1)%7])
else:
    for i in range(m-1):
        total += date_num[i]
    print(day[(total+d-1)%7])