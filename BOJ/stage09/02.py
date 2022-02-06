M = int(input())
N = int(input())

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

prime_lst = []
while (M <= N) :
    if (prime_check(M) == 1) :
        prime_lst.append(M)
    M += 1

if (len(prime_lst) == 0) :
    print(-1)
else :
    print(sum(prime_lst))
    print(prime_lst[0])