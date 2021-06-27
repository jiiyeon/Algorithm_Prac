#조건 : 동적계획법에서 어떤 부분을 저장할 것인지 파악

import sys

#3차원 배열 선언
# a, b, c가 20 이상일 경우 20이라고 줄이므로 dp의 최댓값은 (20,20,20)
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

#주어진 점화식 구현
def     w(a, b, c):
    #조건1 : a 또는 b 또는 c가 음수일때
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    #조건2 : a 또는 b 또는 c가 20 초과일 때
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    #memorization : (a, b, c)에 대하여 함수 w가 계산한 값이 이미 존재한다면 그 값을 불러옴
    # 함수에서 계산이 완료된 후 그 값을 dp[a][b][c]에 저장하도록 구현함
    if dp[a][b][c]:
        return dp[a][b][c]

    #memorizaion 조건문
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    
    #조건3 : w(a, b, c)를 수행했을때 계산되는 값
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1 , b - 1, c - 1)
    return dp[a][b][c]

while 1:
    a, b, c = map(int, sys.stdin.readline().split())

    if all((a == -1, b == -1, c == -1)):
        break

    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))
