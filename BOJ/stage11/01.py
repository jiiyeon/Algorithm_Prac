import sys

size, MAX = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

i = 0
res = 0
while (i < size) :

    j = i + 1
    while (j < size) :

        r = j + 1
        while (r < size) :
            tmp = num[i] + num[j] + num[r]
            if (res < tmp and tmp <= MAX) :
                res = tmp
            r += 1
        j += 1
    i += 1

print(res)