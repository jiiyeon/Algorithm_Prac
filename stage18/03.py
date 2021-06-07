import sys

size = int(sys.stdin.readline())
i = 0
res = []
while i < size:
    stack = [sys.stdin.readline().strip()]

    cnt = 0
    while len(stack) != 0:

        if cnt < 0:
            break

        pop_str = stack.pop()
        if pop_str == ")":
            cnt += 1
        else :
            cnt -= 1
    
    if cnt == 0:
        res.append("YES")
    else :
        res.append("NO")
    i += 1

print("\n".join(res))
