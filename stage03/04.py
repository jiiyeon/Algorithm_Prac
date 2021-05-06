import sys

size = int(sys.stdin.readline().rstrip("\n"))
res = []

for i in range(1, size + 1) :
    n, m = map(int, sys.stdin.readline().rstrip("\n").split())
    res.append(n + m)

for i in range(0, size) :
    print(res[i])