generated_num = set()
normal_num = set(range(1,10001))
for i in range(10001):
    length = len(str(i))
    tmp = 0
    for j in str(i):
        tmp += int(j)
    generated_num.add(tmp+i)

