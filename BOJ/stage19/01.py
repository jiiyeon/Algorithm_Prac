import sys
from collections import deque

def     ft_push(x):
    global  queue

    return  queue.append(x)


def     ft_pop():
    global  queue

    if not queue :
        return (-1)
    else :
        return(queue.popleft())


def     ft_size():
    global  queue

    return(len(queue))


def     ft_empty():
    return 1 if not queue else 0


def     ft_front():
    return queue[0] if queue else -1


def     ft_back():
    return queue[-1] if queue else -1


size = int(sys.stdin.readline())
i = 0
queue = deque([])
while i < size:
    sen = sys.stdin.readline().split()

    if sen[0] == "push":
        ft_push(int(sen[1]))
    elif sen[0] == "pop":
        print(ft_pop())
    elif sen[0] == "size":
        print(ft_size())
    elif sen[0] == "empty":
        print(ft_empty())
    elif sen[0] == "front":
        print(ft_front())
    elif sen[0] == "back":
        print(ft_back())
        
    i += 1
