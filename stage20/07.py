#조건1 : 주어진 행렬을 2차원 배열 데이터로 입력
#조건2 : 행렬의 각 원소를 그대로 곱하면 숫자가 매우 커지므로 나머지 단위에서 어떻게 처리할지 수리적 접근필요

import sys

def     ft_mod(a, b, p):

    #n = a * m + b일 때 n ** 2 = a * (m ** 2) + 2 * a * b * m + b ** 2 = { a * m + 2 * a * b} * m + b ** 2
    # 즉 b의 거듭제곱(m으로 묶었을 때 상수항)을 m으로 나눈 나머지가 원래 수를 m으로 나눈 나머지와 같음
    mod = a % b
    return (mod ** p) % b
    

if __name__ == "__main__":
    N, P = map(int, sys.stdin.readline().split())
    
    #행렬 입력
    A = []
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))

    X = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for m in range(N):
                
            A[i][j] = ft_mod(A[i][j])