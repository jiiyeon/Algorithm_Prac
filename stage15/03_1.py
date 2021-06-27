#조건 : N = (0 세트의 개수) * 2 + (1 카드의 개수)이므로 N = 2 * X + Y가 성립하는 (X, Y)를 구함
# 각 순서쌍을 만족하는 조합의 수는 [x] * X + [y] * Y 원소를 나열하는 경우의 수와 같음
# 즉 ∑(X + Y)! / (X! * Y!)

import sys
from types import resolve_bases

N = int(sys.stdin.readline().rstrip())
dp = [[0]* (N + 1) for _ in range(N + 1)]

def     ft_factorial(n):

    if n <= 1:
        return 1
    return n * ft_factorial(n - 1)

i = 0
res = 0
while i <= N:

    j = 0
    while j <= N:

        if dp[i][j]:
            continue

        elif (2 * i + j) == N:
           dp[i][j] = ft_factorial(i + j) / (ft_factorial(i) * ft_factorial(j))
           res += dp[i][j]
        j += 1
    i += 1

print(res % 15746)
