#조건 : 1이 등장했을때, 해당 노드의 좌우(x ± 1), 상하(y ± 1)에 1이 있는지 확인하는 dfs

import sys

def     dfs(x, y):

    global  cnt

    #방문한 좌표를 0으로 바꾼 후, 같은 단지에 속한 건물 수를 더함
    board[x][y] = 0
    cnt += 1
    for i in range(4):
        
        #i = 0일 때 (nx, ny)는 좌
        # 상하좌우 중 하나로 바꿨을때
        nx = x + dx[i]
        ny = y + dy[i]

        #범위를 벗어나면 확인하지 않음
        if nx < 0 or nx >= size or ny < 0 or ny >= size:
            continue

        #받아온 데이터에가 1인 좌표라면 재귀함수 호출
        if board[nx][ny] == "1":
            dfs(nx, ny)

if __name__ == "__main__":
    size = int(sys.stdin.readline().rstrip())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(size)]

    #상하좌우로 변화시길 변수 선언
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    #같은 단지에 속하는 아파트 개수
    cnt = 0
    cnt_lst = []
    for i in range(size):
        for j in range(size):

            #전체 board를 순회하다가 1을 만나면 같은 단지에 속하는 아파트 카운트 시작
            if board[i][j] == "1":
                cnt = 0
                dfs(i, j)
                cnt_lst.append(cnt)

    sorted(cnt_lst)
    print(len(cnt_lst))
    for num in cnt_lst:
        print(num)
