#조건 : R == 배열의 순서를 반대로하는 함수/ D == 현재 배열에서 첫번째 숫자를 버리는 함수

import sys
from collections import deque

size = int(sys.stdin.readline().rstrip())

def     ft_res(func, length):
    global  deq

    #길이가 0일때 따로 deq따로 설정
    if length == 0:
        deq = deque()
    
    isError = 0
    isReverse = 0
    for d in func:
        #R이 등장했을때 순서가 뒤집힌 배열을 생성하는 것이 아니라, 뽑을 위치를 바꿈
        if d == "R":
            isReverse = not isReverse
        else:
            if not deq:
                isError = True
                break
            if isReverse:
                deq.pop()
            else:
                deq.popleft()
    
    if not isError:
        if isReverse:
            deq.reverse()
        value = list(deq)
    else:
        value = "error"

    return value

i = 0
res_lst = []
while i < size:
    func = list(sys.stdin.readline().rstrip())
    length = int(sys.stdin.readline().rstrip())
    deq = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    res_lst.append(ft_res(func, length))
    i += 1

i = 0
while i < size:

    if res_lst[i] == "error":
        print(res_lst[i])
    #출력형식에서 list 원소사이에 여백이 있으면 안 됨. 따라서 예제형식에 맞춰 print 영역 별도로 설정
    else:
        print("[", end="")
        print(",".join(res_lst[i]), end="")
        print("]")
    i += 1
