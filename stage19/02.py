import sys
from collections import deque

N = int(sys.stdin.readline().strip())
N_queue = deque([x for x in range(1, N + 1)])

while 1:
    
    if len(N_queue) == 1:
        print(N_queue[0])
        break
    
    N_queue.popleft()
    N_queue.append(N_queue.popleft())
