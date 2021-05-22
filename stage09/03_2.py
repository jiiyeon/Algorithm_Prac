N = int(input())

i = 2
prime_lst = []
while (i < N) :

    j = 2
    flag = 1
    while (j < i) :
        if (i % j == 0) :
            flag = 0
            break
        j += 1
    if (flag == 1) :
        prime_lst.append(i)
    i += 1

i = 0
while (1) :
    if (N == 1) :
        break
    while (N % prime_lst[i] == 0) :
        print(prime_lst[i])
        N /= prime_lst[i]
    i += 1