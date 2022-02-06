import sys

size = int(sys.stdin.readline().strip())
num_lst = []
i = 0
while i < size:
    num_lst.append(int(sys.stdin.readline().strip()))
    i += 1

i = 0
tmp = ""
while i < size:

    r = i + 1
    while r < size:

        if num_lst[i] > num_lst[r]:
            num_lst[i], num_lst[r] = num_lst[r], num_lst[i]
        r += 1
    i += 1

i = 0
while i < size:
    print(num_lst[i])
    i += 1
