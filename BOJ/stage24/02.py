#조건 : 1번과 연결되어있는 컴퓨터 찾기

import sys

def     dfs(V):

    visited[V] = 1
    for i in range(N + 1):

        #현재 노드 중 방문한 적없고 V와 연결된 곳이 있다면 그 노드로 이동(재귀호출)
        if (visited[i] == 0 and matrix[V][i] == 1):
            dfs(i)

if __name__ == "__main__":
    
    #N : 노드 수/ M : 간선 수
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = matrix[b][a] = 1
    
    #1번 컴퓨터와 연결된 컴퓨터만 찾았을 때, 해당 노드에 대해서만 visited[i]값이 1이됨
    dfs(1)
    cnt = 0
    for i in range(2, N + 1):
        if visited[i] == 1:
            cnt += 1
    print(cnt)
