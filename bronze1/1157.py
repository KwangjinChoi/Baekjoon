from collections import Counter
string = input()
cnt = Counter(string.upper())
if len(cnt) == 1:
    print(cnt.most_common(1)[0][0])
else:
    tmp = cnt.most_common(2)
    if tmp[0][1] == tmp[1][1]:
        print('?')
    else:
        print(tmp[0][0])