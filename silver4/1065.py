N = int(input())
if N <= 99:
    res = N
else:
    res = 99
    for i in range(100, N+1):
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            res += 1

print(res)       