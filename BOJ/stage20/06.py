#조건1 : 크기가 정해지지 않은 두 행렬의 데이터 받아오기
#조건2 : 두 행렬을 곱한 행렬을 출력

import sys

if __name__ == "__main__":

    #A를 2차원 배열로 입력
    N, M = map(int, sys.stdin.readline().split())
    A = []
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
    
    #B를 2차원 배열로 입력
    M, K = map(int, sys.stdin.readline().split())
    B = []
    for j in range(M):
        B.append(list(map(int, sys.stdin.readline().split())))
    
    #행렬 곱
    X = [[0] * K for _ in range(N)]
    for n in range(N):
        for k in range(K):
            for m in range(M):
                X[n][k] += A[n][m] * B[m][k]
    
    for row in X:
        print(*row)
