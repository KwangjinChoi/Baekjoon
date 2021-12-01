import sys
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums = sorted(nums)
for i in nums:
    print(i)
