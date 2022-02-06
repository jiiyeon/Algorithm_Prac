import sys

size = int(sys.stdin.readline().rstrip())

i = 0
num_lst = []
while i < size:
    num = int(sys.stdin.readline().rstrip())
    num_lst.append(num)
    i += 1

def     num_seq():

    cnt = 1
    stack = []
    res = []
    for i in num_lst:
        while cnt <= i:
            stack.append(cnt)
            res.append("+")
            cnt += 1
        if stack.pop() != i:
            return "NO"
        else:
            res.append("-")
    return "\n".join(res)

print(num_seq())
