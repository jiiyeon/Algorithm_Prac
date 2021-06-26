#조건 : 하나의 배열에서 상하좌우를 확인하지 않고, 한 좌표에 대해 3가지 배열을 선언하여 동시에 확인함 

import sys

size = int(sys.stdin.readline().rstrip())

y = [False] * size
diag_up = [False] * (2 * size - 1)
diag_down = [False] * (2 * size - 1)
queen = 0

def     ft_queen(x):
    global  queen

    if x == size:
        queen += 1
        return
    
    #N * N board (X, Y)좌표의 오른쪽 위 대각선 방향 좌표의 일반항 == X + Y
    #N * N board (X, Y)좌표의 오른쪽 아래 대각선 방향 좌표의 일반항 == (X - Y) + (N - 1)
    for i in range(size):
        if not (y[i] or diag_up[x + i] or diag_down[x - i + size - 1]):
            
            #이 부분이 백트래킹 구조 : append -> 재귀 -> pop
            y[i] = diag_up[x + i] = diag_down[x - i + size - 1] = True
            ft_queen(x + 1)
            y[i] = diag_up[x + i] = diag_down[x - i + size - 1] = False

ft_queen(0)
print(queen)
