#조건1 : 가로줄, 세로줄에 숫자 당 1회만 등장
#조건2 : 한 그룹(작은 박스)에 숫자 당 1회만 등장
# 빈 칸이 있는 스도쿠 보드가 주어졌을 때, 빈 칸에 들어갈 숫자를 채움

import sys

#입력을 받아서 2차원 배열로 저장
condition = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

#board 구성
# sub도 1 ~ 9를 확인하는 용도이므로 네모모양을 만들 필요 없음
# board를 2차원 배열로 쓰지 않고 (X, Y) -> 9 * X + Y 값으로 보고 1차월 배열로 선언 
board = [0] * 81
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
sub = [[False] * 10 for _ in range(9)]

#func1 : sub 번호
def     ft_sub(i, j):
    return (i // 3) * 3 + j // 3

#func2 : sudoku
def     sudoku(idx):
    if idx == n:
        for i in range(9):
            print(*condition[i])
        #첫번째로 완성한 condition을 print하므로 조건만족시 코드 종료
        exit(0)
    #숫자가 빈 좌표 불러오기
    x = board[idx] // 9
    y = board[idx] % 9

    for i in range(1, 10):

        #i가 가로, 세로, 그룹 안에서 사용된 적 없는 숫자일 때
        if not (row[x][i] or col[y][i] or sub[ft_sub(x, y)][i]):
            #해당 숫자를 condition에 넣고 가로, 세로, 그룹에 숫자를 넣었다고 표시함
            condition[x][y] = i
            row[x][i] = col[y][i] = sub[ft_sub(x, y)][i] = True
            sudoku(idx + 1)
            condition[x][y] = 0
            row[x][i] = col[y][i] = sub[ft_sub(x, y)][i] = False

#row, col, sub에서 condition에 사용된 숫자는 True로 전환
# condition에서 0으로 주어진 칸의 개수 == n
n = 0
for i in range(9):
    for j in range(9):
        tmp = condition[i][j]
        if tmp:
            row[i][tmp] = True
            col[j][tmp] = True
            sub[ft_sub(i, j)][tmp] = True
        else:
            board[n] = i * 9 + j
            n += 1

sudoku(0)
