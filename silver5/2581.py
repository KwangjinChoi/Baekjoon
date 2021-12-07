M = int(input())
N = int(input())

def prime_list(M, N):
    prime = [False, False] + [True] * N
    for i in range(1, int(N**0.5)+1):
        if prime[i] == True:
            for j in range(i+i, N+1, i):
                prime[j] = False
    return [i for i in range(2, N+1) if (prime[i] == True and (M <= i <= N))]

prime = prime_list(M, N)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
