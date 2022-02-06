import sys

size = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

def     right_max(int):
    global  data

    num = data[int]

    i = int + 1
    stack = []
    while i < size:
        if data[i] > num:
            stack.append(data[i])
            break
        i += 1
    
    if stack:
        return stack.pop()
    else:
        return -1

i = 0
res = []
while i < size:
    res.append(right_max(i))
    i += 1

for item in res:
    print(item, end=" ")
