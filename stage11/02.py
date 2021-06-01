import sys

def     div_sum(INIT) :

    Goal = int(INIT)

    #시간이 오래걸리므로 초기값의 자릿수에 맞춰서 생성자를 찾기 시작함
    n = Goal - 9 * (len(INIT) - 1)
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