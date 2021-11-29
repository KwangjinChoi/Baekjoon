S = input()
res = ''

for i in range(26):
    cnt = 0
    for index, j in enumerate(S):
        if (ord(f'{j}') - ord('a')) == i:
            idx = index
            break
        else:
            cnt += 1
    if cnt == len(S):
        res += '-1 '
    else:
        res += f'{idx} '
print(res)
