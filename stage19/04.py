import sys
from collections import deque

size = int(sys.stdin.readline().rstrip())

def     ft_prior(length, idx, que):

    cnt = 0
    while 1:
        out = que.popleft()
        flag = 0

        for num in que:
            if num > out:
                que.append(out)
                if idx != 0:
                    idx -= 1
                else:
                    idx = len(que) - 1
                flag = 1
                break
        if not flag:
            cnt += 1
            if idx == 0:
                break
            else:
                idx -= 1
    return(cnt)

i = 0
cnt_lst = []
while i < size:
    length, idx = map(int, sys.stdin.readline().split())
    que = deque(list(map(int, sys.stdin.readline().split())))
    cnt_lst.append(ft_prior(length, idx, que))
    i += 1
print(*cnt_lst)