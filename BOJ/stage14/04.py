import sys

size, value = map(int, sys.stdin.readline().split())

case = []
def     dfs_next(depth, start):

    if depth == value:
        print(*case)
        return

    for num in range(start, size + 1):
        case.append(num)
        dfs_next(depth + 1, num)
        check_pt = case.pop()

dfs_next(0, 1)
