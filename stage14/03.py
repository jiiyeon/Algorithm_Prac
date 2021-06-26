import sys

size, value = map(int, sys.stdin.readline().split())

case = []
def     dfs_plus():
    if len(case) == value:
        print(*case)
        return
    
    for num in range(1, size + 1):
        case.append(num)
        dfs_plus()
        case.pop()

dfs_plus()
