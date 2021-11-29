N = input().strip()
cnt = 1
tmp = N
while True:
    if len(tmp) == 1:
        tmp = '0' + N
    f, s = map(int, tmp[:])
    tmp = str(s) + str((f + s)%10)
    if int(tmp) == int(N):
        break
    else:
        cnt += 1
print(cnt)
        