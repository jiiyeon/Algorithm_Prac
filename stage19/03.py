import sys
from collections import deque
from typing import no_type_check_decorator

N, K = map(int, sys.stdin.readline().split())
N_deque = deque([x for x in range(1, N + 1)])
res = []

while N_deque:
    N_deque.rotate(-(K - 1))
    res.append(N_deque.popleft())

print("<", end="")
i = 0
while 1:
    if i == len(res) - 1:
        print(res[i], end=">")
        break

    print(res[i], ", ", sep="", end="")
    i += 1
