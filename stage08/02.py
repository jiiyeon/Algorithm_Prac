N = int(input())

def     arith_num(N) :

    sum = 1
    i = 0
    while (1) :
        layer = 6 * i
        sum += layer
        i += 1

        if (sum >= N) :
            break

    return (i)

print(arith_num(N))