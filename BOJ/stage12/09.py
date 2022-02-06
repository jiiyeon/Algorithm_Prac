import sys

size = int(sys.stdin.readline())
i = 0
data = []
while i < size:
    age, name = sys.stdin.readline().split()
    age = int(age)
    data.append((i, age, name))
    i += 1

sort_data = sorted(data, key=lambda x: (x[1], x[0]))
i = 0
while i < size:
    print(sort_data[i][1], sort_data[i][2], sep=" ")
    i += 1
