size = int(input())
num_lst = list(map(int, input().split()))

def     prime_check(int) :

    n = 1
    flag = 1
    while (n <= int) :
        if ((int == 1) or (int / n == 0)) :
            flag = 0
            break
        n += 1
    
    return(flag)

i = 0
cnt = 0
while (i < size) :
    if (prime_check(num_lst[i]) == 1) :
        cnt += 1
    i += 1
print(cnt)