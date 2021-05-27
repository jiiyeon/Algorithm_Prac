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

#test case 입력
i = 0
test_lst = []
while (i < size) :
    N = int(input())
    test_lst.append(N)
    i += 1

#차이가 작은 골드바흐 파티션을 출력하므로 가운데 지점부터 시작
i = 0
a = 0
while (i < size) :
    prime_lst = ft_prime_lst(test_lst[i])
    N = len(prime_lst)
    
    m = 0
    a_lst = []
    b_lst = []
    while (m < N) :

        n = m
        while (n < N) :
            if (prime_lst[m] + prime_lst[n] == test_lst[i]) :
                a_lst.append(prime_lst[m])
                b_lst.append(prime_lst[n])
            n += 1
        m += 1
    print(a_lst[-1], b_lst[-1], sep=" ")
    i += 1