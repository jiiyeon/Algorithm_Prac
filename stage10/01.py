import sys

def     ft_factorial(int) :
    res = 1
    
    #int == 0 or 1 일 경우에는 값이 항상 1이므로 재귀에 포함시키지 않음
    if (int > 0) :
        res = int * ft_factorial(int - 1)

    return(res)

n = int(sys.stdin.readline())
print(ft_factorial(n))