#조건 : 각 수가 정수 최대 범위로 들어올 수 있으므로 바로 거듭제곱을 하면 오버플로우 발생할 수 있음

import sys

def     solve(b):
    if b == 0:
        return 1

    if b == 1:
        return A % C
    else:

        #분배법칙 규칙 이용
        if b % 2 == 0:
            return (solve(b // 2) ** 2) % C
        else:
            return (solve(b // 2) ** 2 * A) % C

if __name__ == "__main__":
    A, B, C  = map(int, sys.stdin.readline().split())
    
    print(solve(B))
