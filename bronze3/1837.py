P, K = map(int, input().split(' '))

prime = [False, False] + [True] * (K-2)
primes = []
for i in range(2, K):
    if prime[i]:
        primes.append(i)
        for j in range(2*i, K, i):
            prime[j] = False

res = 'GOOD'
for i in primes:
    if P%i == 0:
        res = f'BAD {i}'
        break
print(res)