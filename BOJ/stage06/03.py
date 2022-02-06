N = int(input())

def     arith_check(num1) :

    num_lst = list(str(num1))
    i = 0
    res = 0
    while (i < len(num_lst)) :
        num_lst[i] = int(num_lst[i])
        i += 1

    if (len(num_lst) == 1) :
        res += 1
    elif (len(num_lst) == 2) :
        res += 1
    else :
        if (num_lst[2] == num_lst[0] + (3 - 1) * (num_lst[1] - num_lst[0])) :
            res += 1
    
    return (res)

i = 1
cnt = 0
while (i <= N) :
    if (arith_check(i) == 1) :
        cnt += 1
    i += 1
print(cnt)