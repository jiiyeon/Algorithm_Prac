M, N = map(int, input().split())

def     prime_check(int) :

    flag = 1

    if (int == 1) :
        flag = 0
        return(flag)

    n = 2
    while (n < int) :
        if (int % n == 0) :
            flag = 0
            break
        n += 1
    
    return(flag)

while (M <= N) :
    if (prime_check(M) == 1) :
        print(M)
    M += 1