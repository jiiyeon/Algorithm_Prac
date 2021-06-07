import sys

raw = sys.stdin.readline().strip().split(".")
print(raw)

i = 0
res = []
while i < len(raw):

    data = list(raw[i])
    cnt_lst = [0, 0]
    r = 0
    while r < len(data):

        if (cnt_lst[0] < 0) or (cnt_lst[1] < 0):
            break

        word = data.pop()
        if word == ")":
            cnt_lst[0] += 1
        elif word == "(":
            cnt_lst[0] -= 1
        elif word == "]":
            cnt_lst[1] += 1
        elif word == "[":
            cnt_lst[1] -= 1
        r += 1
    if (cnt_lst[0] == 0) and (cnt_lst[1] == 0):
        res.append("YES")
    else :
        res.append("NO")
    i += 1

print("\n".join(res))
