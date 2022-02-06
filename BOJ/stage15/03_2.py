#조건 : n칸에 대해 만들 수 있는 경우의 수가 dp[n] = dp[n - 1] + dp[n - 2]를 만족하는 피보나치 수열이 됨

import sys

N = int(sys.stdin.readline().rstrip())

#dp : n칸에 대한 경우의수 % 15746 값을 넣는 1차원 배열
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

i = 3
while i <= N:
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    i += 1

print(dp[N])
