P, K = map(int, input().split(' '))

primes = []


def good_or_bad(P, K):
    for i in range(1, K):
        if is_prime(i) and P%i==0:
            r = int(P/i)
            if is_prime(r):
                res=r if r<i else i
                return 'BAD '+ str(res)
    return 'GOOD'

res = good_or_bad(P, K)
print(res)