import sys

def     div_sum(INIT) :

    Goal = int(INIT)

    n = 1
    while (1) :

        res = n

        i = 0
        tmp = n
        while (tmp != 0) :
            res += tmp % 10
            tmp //= 10

        if (res == Goal) :
            return(n)
        
        elif (n > Goal) :
            return(0)
        
        n += 1

INIT = sys.stdin.readline().strip()
print(div_sum(INIT))