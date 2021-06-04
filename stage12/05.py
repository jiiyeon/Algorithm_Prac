import sys

num_lst = list(sys.stdin.readline().strip())
num_lst = sorted(num_lst, reverse=True)

print("".join(num_lst))