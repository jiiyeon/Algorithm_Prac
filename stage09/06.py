size = int(input())

#에라토스테네스의 체 정의
def     ft_prime_lst(N) :
    sieve = [False] + [True] * (N -  1)

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

#차이가 가장 적은 케이스를 출력하므로 index = N // 2 부터 시작
i = 0
while (i < size) :
    NUM = int(input())
    prime_lst = ft_prime_lst(NUM)
    N = len(prime_lst)

    m = max([x for x in range(0, len(prime_lst)) if prime_lst[x] <= NUM  // 2])
    flag = 1
    while (m >= 0) :

        if (flag == 0) :
            break

        n = m
        while (n < N) :
            if (prime_lst[m] + prime_lst[n] == NUM) :
                print(prime_lst[m], prime_lst[n], sep=" ")
                flag = 0
            n += 1
        m -= 1
    i += 1