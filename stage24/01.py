#조건 : DFS와 BFS 개념 비교
# DFS : 깊이 우선 탐색. 한 정점에서 이어진 다른 정점의 끝까지 간다음 돌아가기를 반복
# BFS : 너비 우선 탐색. 한 정점과 이어진 모든 정점을 들른 후 다음 정점에서도 반복

import sys

#case1 : dfs
def     dfs(V):
    visited[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):

        #전체 노드 중 만약 방문한 적 없고, 현재 노드와 연결된 노드가 있다면 거기로 이동
        # 재귀를 호출하여 연결된 곳을 먼저 방문하고 print
        if (visited[i] == 0 and matrix[V][i] == 1):
            dfs(i)

#case2 : bfs    
def     bfs(V):

    #queue로 들러야할 정점 저장
    que = [V]
    visited[V] = 1
    while que:

        #2 for문을 돌며 큐를 완성해서 빠져나오면 while문에서 먼저 들어간 순서대로 pop
        # pop() : 가장 나중의 원소/ pop(0) : 가장 처음의 원소
        V = que.pop(0)
        print(V, end=" ")
        for i in range(1, N + 1):

            #1 전체 노드 중 만약 방문한 적 없고, 현재 노드와 연결된 노드가 있다면 그 노드를 큐에 저장
            if (visited[i] == 0 and matrix[V][i] == 1):
                que.append(i)
                visited[i] = 1

#N : 정점의 개수/ M : 간선의 개수/ V : 시작점
if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    matrix = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        #matrix에 연결되어있는 노드 저장
        matrix[a][b] = matrix[b][a] = 1
    
    #dfs
    visited = [0] * (N + 1)
    dfs(V)
    print()

    #bfs
    visited = [0] * (N + 1)
    bfs(V)
