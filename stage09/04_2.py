#에라토스테네스의 체 정의

def     ft_prime_lst(N) :
    #초기화 (1은 소수가 아니므로 False로 시작)
    sieve = [False] + [True] * (N -  1)
    print(sieve)

    mid = int(N ** 0.5)
    i = 1
    while (i < mid) :
        if (sieve[i] == True) :

            j = i + 1
            while (i + j < N) :
                sieve[i + j] = False
                j += j
        i += 1
    print(sieve)
    
    prime_lst = []
    i = 1
    while (i < N) :
        if (sieve[i] == True) :
            prime_lst.append(i + 1)
        i += 1
    
    return (prime_lst)

N = int(input())
print(ft_prime_lst(N))
