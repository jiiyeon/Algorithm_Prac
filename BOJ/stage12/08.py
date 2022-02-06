import sys

size = int(sys.stdin.readline())
i = 0
data = []
while i < size:
    string = sys.stdin.readline().strip()
    data.append(string)
    i += 1

sort_data = sorted(set(data), key=lambda x: (len(x), x))
i = 0
while i < len(sort_data):
    print(sort_data[i])
    i += 1
