import sys

def     ft_push(x):
    global  stack

    return  stack.append(x)

def     ft_pop():
    global  stack

    if not stack :
        return (-1)
    else :
        return(stack.pop())

def     ft_size():
    global  stack

    return(len(stack))

def     ft_empty():
    return 1 if not stack else 0

def     ft_top():
    return stack[-1] if stack else -1

size = int(sys.stdin.readline())
i = 0
stack = []
while i < size:
    sen = sys.stdin.readline().split()

    if sen[0] == "push":
        ft_push(sen[1])
    elif sen[0] == "pop":
        print(ft_pop())
    elif sen[0] == "size":
        print(ft_size())
    elif sen[0] == "empty":
        print(ft_empty())
    elif sen[0] == "top":
        print(ft_top())
    i += 1
