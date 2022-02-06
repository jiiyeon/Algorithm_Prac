import sys

size = int(sys.stdin.readline())
i = 0
stack = []
while i < size:
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else :
        stack.append(num)
    i += 1

print(sum(stack))
