#조건1 : n층 원반을 옮기기 위해서 1부터 (n - 1)까지이 원반이 다른 자리로 이동해야함
# n이 짝수일 경우에는 2번자리, n이 홀수일 경우 3번자리로 먼저 이동함
#조건2 : 원판의 이동경로를 순서쌍으로 받아오며, 맨 첫줄에 순서쌍의 개수를 출력함

import sys

def     hanoi(int, s1, s2, s3) :
    global  path

    if (int == 1) :
        path.append([s1, s3])
        return
    
    hanoi(int - 1, s1, s3, s2)
    path.append([s1, s3])
    hanoi(int - 1, s2, s1, s3)

path = []
N = int(sys.stdin.readline())
hanoi(N, 1, 2, 3)

print(len(path))
print("\n".join([" ".join(str(i) for i in row) for row in path]))