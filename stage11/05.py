import sys

N = int(sys.stdin.readline())

num_lst = [666]
n = 1666
while (1) :

    if (len(num_lst) == N) :
        break

    tmp = str(n)
    i = 0
    while (i + 2 < len(tmp)) :

        if ((tmp[i] == '6') and (tmp[i + 1] == '6') and (tmp[i + 2] == '6')) :
            num_lst.append(n)
            break
        i += 1
    n += 1

print(num_lst[N - 1])