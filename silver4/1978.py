def get_prime(N):
    primes = [False, False] + [True] * N
    for i in range(2, int(N**0.5)+1):
        if primes[i] == True:
            for j in range(i+i, N+2, i):
                primes[j] = False
    return [i for i in range(1, N+1) if primes[i] == True]

n = int(input())
nums = list(map(int, input().split()))
primes = get_prime(max(nums))
res = 0
for i in nums:
    if i in primes:
        res += 1

print(res)