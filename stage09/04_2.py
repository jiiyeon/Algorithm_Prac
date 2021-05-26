#에라토스테네스의 체 정의
def     ft_prime_lst(N) :
    #초기화 (1은 소수가 아니므로 False로 시작)
    sieve = [False] + [True] * (N -  1)

    #최대 약수까지만 검사
    mid = int(N ** 0.5)
    i = 1
    while (i < mid) :
        if (sieve[i] == True) :

            j = i + 1
            while (i + j < N) :
                sieve[i + j] = False
                j += (i + 1)
        i += 1
    
    prime_lst = []
    i = 1
    while (i < N) :
        if (sieve[i] == True) :
            prime_lst.append(i + 1)
        i += 1
    
    return (prime_lst)

M, N = map(int, input().split())
prime_lst = ft_prime_lst(N)

i = 0
while (i < len(prime_lst)) :
    if (prime_lst[i] >= M) :
        print(prime_lst[i])
    i += 1