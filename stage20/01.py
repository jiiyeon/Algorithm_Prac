#조건 : 쿼드트리 == 조건이 만족되지 않으면 4개로 쪼개어 다시 품

import sys

def     solve(x, y, size):

    global  white, blue

    check = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):

            #현재 범위에서 (x, y)값과 다른 값이 하나라도 있으면 재귀로 4분할 호출
            if check != board[i][j]:
                #1사분면
                solve(x, y, size // 2)
                #2사분면
                solve(x, y + size // 2, size // 2)
                #3사분면
                solve(x + size // 2, y, size // 2)
                #4사분면
                solve(x + size // 2, y + size // 2, size // 2)
                return
    
    #값이 0일때 white, 1일때 blue
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


if __name__ == "__main__":
    size = int(sys.stdin.readline().rstrip())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]

    white = 0
    blue = 0
    solve(0, 0, size)
    print(white, blue, sep="\n")
