#조건1: size의 deque을 만들고, 주어진 리스트를 만들기 위해서 deque의 순서를 총 몇 번 변경해야하는지 구함 

import sys
from collections import deque

size, last = map(int, sys.stdin.readline().split())
value = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, size + 1)])

cnt = 0
for idx in value:
    while 1:
        #구하고자하는 값이 deque의 맨 처음에 있는 경우
        if deq[0] == idx:
            deq.popleft()
            break
        #순서를 바꿔야하는 경우
        else:
            #구하고자하는 값의 index가 deque의 앞부분에 위치한 경우 : deque 맨 앞의 숫자를 pop
            if deq.index(idx) < len(deq) / 2:
                while deq[0] != idx:
                    deq.append(deq.popleft())
                    cnt += 1
            #구하고자하는 값의 index가 deque의 뒷부분에 위치한 경우 : deque 맨 뒤의 숫자를 pop
            else:
                while deq[0] != idx:
                    deq.appendleft(deq.pop())
                    cnt += 1
print(cnt)
