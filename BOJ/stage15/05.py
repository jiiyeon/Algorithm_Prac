#조건 : 연속한 집의 색깔이 달라야함
# dp[i][color_idx]에 i번째집에 color_index를 칠했을 때의 최소 비용을 저장함
# 즉 dp[i][color_idx]는 바로 전에서 나머지 두 색상에서 발생하는 총 비용 중 더 작은 값 + 현재 집을 칠하는 비용
# dp[i][color_idx] = cost[i][color_index] + min(dp[i - 1][other_color_1], dp[i - 1][other_color_2])

import sys

def     solve(size, dp, cost):
    for i in range(size):
        #첫번째 집은 앞서 들어간 비용을 더할 수 없음
        if i == 0:
            dp[i][0] = cost[i][0]
            dp[i][1] = cost[i][1]
            dp[i][2] = cost[i][2]
            continue

        #i번째 집에 color_idx를 칠할때까지 들어간 총 비용
        # case1 : i번째 집에 R을 칠함
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])

        # case2 : i번째 집에 G를 칠함
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])

        # case3 : i번재 집에 B를 칠함
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    #마지막 집까지 칠한 총 비용은 dp에서 마지막 row을 보면 알 수 있음
    # 마지막 집의 색상이 R,G,B인 경우 중 비용이 가장 작은 값 선택
    total_min = min(dp[size - 1][0], dp[size - 1][1], dp[size - 1][2])

    return total_min

#시작함수
if __name__ == "__main__":
    size = int(sys.stdin.readline().rstrip())
    cost = []
    for _ in range(size):
        value = list(map(int, sys.stdin.readline().split()))
        cost.append(value)
    
    dp = [[0] * 3 for _ in range(size)]
    print(solve(size, dp, cost))
