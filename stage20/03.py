#조건 : 쿼드트리 문제풀이 방식으로 9분할면에 적용

import sys

def     solve(x, y, size):
    global zero, minus, plus

    check = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):

            #현재 범위에서 (x, y)값과 다른 값이 하나라도 있으면 재귀로 3 * 3분할 호출
            if board[i][j] != check:
                k = size // 3

                # 차례대로 윗줄부터 9개 분할면 표현
                solve(x, y, k)
                solve(x + k, y, k)
                solve(x + 2 * k, y, k)
                

if __name__ = "__main__":
    size = int(sys.stdin.readline().rstrip())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

    zero = 0
    minus = 0
    plus = 0