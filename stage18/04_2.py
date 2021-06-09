import sys

res = []
while 1:
    raw = sys.stdin.readline().rstrip("\n")

    #입력으로 "."만 받을 때까지 반복
    if raw == ".":
        break

    stack = []
    flag = 1
    for w in raw:

        #case1 : 왼쪽 괄호들
        if (w == "(") or (w == "["):
            stack.append(w)
        
        #case2 : 오른쪽 소괄호
        elif (w == ")"):
            if (not stack) or (stack[-1] != "("):
                flag = 0
                break
            elif stack[-1] == "(":
                stack.pop()
        
        #case3 : 오른쪽 대괄호
        elif (w == "]"):
            if (not stack) or (stack[-1] != "["):
                flag = 0
                break
            elif stack[-1] == "[":
                stack.pop()

    if not stack and flag == 1:
        res.append("yes")
    else :
        res.append("no")

print("\n".join(res))
