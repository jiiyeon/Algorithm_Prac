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

i = 2
while (i <= N) :
    if (N == 1) :
        break
    elif (prime_check(i) == 1) :
        while (N % i == 0) :
            print(i)
            N /= i
    i += 1