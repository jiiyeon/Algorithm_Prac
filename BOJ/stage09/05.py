#에라토스테네스의 체를 활용하여 소수 개수 집계
def     ft_prime_lst(N) :
    #초기화 (1은 소수가 아니므로 False로 시작)
    sieve = [False] + [True] * (2 * N -  1)

    #최대 약수까지만 검사
    mid = int((2 * N) ** 0.5)
    i = 1
    while (i < mid) :
        if (sieve[i] == True) :

            j = i + 1
            while (i + j < 2 * N) :
                sieve[i + j] = False
                j += (i + 1)
        i += 1
    
    prime_lst = []
    i = N
    while (i < 2 * N) :
        if (sieve[i] == True) :
            prime_lst.append(i + 1)
        i += 1
    
    return (len(prime_lst))

i = 0
cnt_lst = []
while (1) :
    N = int(input())
    if (N == 0) :
        break

    cnt_lst.append(ft_prime_lst(N))
    i += 1

i = 0 
while (i < len(cnt_lst)) :
    print(cnt_lst[i])
    i += 1