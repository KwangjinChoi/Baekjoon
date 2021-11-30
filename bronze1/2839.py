N = int(input())
res = -1
for i in range(N//5,-1,-1):
    if (N-5*i)%3 == 0:
        res = i+(N-5*i)//3
        break
print(res)