import sys

size = int(sys.stdin.readline())

i = 0
data = []
while i < size:
    M, N = map(int, sys.stdin.readline().split())
    data.append((M, N))
    i += 1

# 정렬 우선순위 : x > y
sort_data = sorted(data, key=lambda x: (x[0], x[1]))
i = 0
while i < size:
    print(sort_data[i][0], sort_data[i][1])
    i += 1
