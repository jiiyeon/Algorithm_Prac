#조건 : 백트래킹 == dfs 기반으로 stack을 이용해 후진함. 브루트포스 전략에서 가지치기를 접목하는 것이 중요.

import sys

size, value = map(int, sys.stdin.readline().split())
num_lst = [x for x in range(1, size + 1)]

#case : stack으로 활용
case = []
def     dfs():
    #case의 길이가 value가 되면 값을 print하고 반환함
    if len(case) == value:
        print(*case)
        return

    for i in num_lst:
        #case에 이미 들어있을 경우 넘어감
        if i in case:
            continue
        case.append(i)
        dfs()
        case.pop()

dfs()
