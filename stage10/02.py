import sys

def     ft_fibo(int) :
    if (int <= 1) :
        return (int)
    return (ft_fibo(int - 1) + ft_fibo(int - 2))

n = int(input())
print(ft_fibo(n))