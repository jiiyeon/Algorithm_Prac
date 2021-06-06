import sys

size = int(sys.stdin.readline().strip())
num_lst = []
i = 0
while i < size:
    num_lst.append(int(sys.stdin.readline().strip()))
    i += 1

for num in sorted(num_lst):
    print(num)
