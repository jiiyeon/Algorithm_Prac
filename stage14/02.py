#조건 : 중복을 허락하지 않으므로 방문여부를 기록하는 배열이 필요

import sys

size, value = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(size)]

#case는 stack으로 활용함
case = []
def     dfs_visit():
    #case 원소의 개수가 value일 경우 return
    if len(case) == value:
        print(*case)
        return

    #visited와 함께 처리하기 위해서 index 기반으로 조건문/반복문 실행
    for i in range(size):
        #중복체크 : 방문하지 않은 수에 대해서
        if visited[i] == 0:
            visited[i] = 1
            case.append(i + 1)
            dfs_visit()
            case.pop()

            #case를 꺼낸 후 다음 부분만 확인하기 위해서 visited를 i + 1부터 초기화
            for r in range(i + 1, size):
                visited[r] = 0

dfs_visit()
