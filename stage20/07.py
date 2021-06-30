#조건1 : 주어진 행렬을 2차원 배열 데이터로 입력
#조건2 : 행렬의 각 원소를 그대로 곱하면 숫자가 매우 커지므로 나머지 단위에서 어떻게 처리할지 수리적 접근필요
#조건3 : 시간 복잡도를 고려하여 logP만큼 수행

import sys

# 조건2 구현
def     ft_multi_mod(A, B, N):

    X = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                X[i][j] += A[i][k] * B[k][j]
                X[i][j] %= 1000
    return X    

#시작함수
# 조건3 적용
if __name__ == "__main__":
    N, p = map(int, sys.stdin.readline().split())
    
    #행렬 입력
    A = []
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))

    E = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
    X = []
    #p == 1로 주어진 경우 아래 반복문을 거치지 않으므로 X가 빈 배열인채로 ft_multi_mod에 들어감
    # 따라서 이 경우 X = E로 선언
    if p == 1:
        X = E

    while p != 1:

        tmp = A[:]
        if p % 2:
            X = ft_multi_mod(E, A, N)
            p -= 1
        else:
            A = ft_multi_mod(tmp, tmp, N)
            p //= 2
            
    X = ft_multi_mod(X, A, N)
    for row in X:
        print(*row)
