from collections import deque
import sys

size = int(sys.stdin.readline().rstrip())

def     push_front(X):
    global  deq

    return deq.appendleft(X)

def     push_back(X):
    global  deq

    return deq.append(X)

def     pop_front():
    global  deq

    if not deq:
        return (-1)
    else:
        return deq.popleft()

def     pop_back():
    global  deq

    if not deq:
        return (-1)
    else:
        return deq.pop()

def     ft_size():
    return len(deq)

def     ft_empty():
    if not deq:
        return 1
    else:
        return 0

def     ft_front():
    if deq:
        return deq[0]
    else:
        return -1

def     ft_back():
    if deq:
        return deq[-1]
    else:
        return -1

i = 0
deq = deque([])
print_lst = []
while i < size:
    sen = list(sys.stdin.readline().split())

    if sen[0] == "push_front":
        push_front(sen[1])
    elif sen[0] == "push_back":
        push_back(sen[1])
    elif sen[0] == "pop_front":
        print_lst.append((pop_front()))
    elif sen[0] == "pop_back":
        print_lst.append((pop_back()))
    elif sen[0] == "size":
        print_lst.append((ft_size()))
    elif sen[0] == "empty":
        print_lst.append((ft_empty()))
    elif sen[0] == "front":
        print_lst.append((ft_front()))
    elif sen[0] == "back":
        print_lst.append((ft_back()))
    i += 1

i = 0
while i < len(print_lst):
    print(print_lst[i])
    i += 1
