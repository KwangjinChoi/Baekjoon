n = int(input())
Fn = [0, 1]
for i in range(2, n+1):
    Fn.append(Fn[i-1]+Fn[i-2])
print(Fn[-1])
