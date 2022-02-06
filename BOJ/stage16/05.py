#조건 : 기름값 예산을 최소한으로 책정하기
# A → B → C로 갈 때, B도시에 도착했는데 A도시의 기름값이 더 쌀 경우 A도시의 기름값으로 예산을 책정하면됨. (코드에서 돌아가는 것이 아님)

import sys

def     solve():
    res = 0
    oilMin = oil_lst[0]

    for i in range(size - 1):

        #현재 도시의 기름값과 지금까지 기름값 중 최솟값을 비교하여 현재도시가 더 작으면 최솟값 변경
        # 이전 최솟값이 더 작을 경우 최솟값인 도시에서 i → (i + 1) 경로에서 필요한 기름을 충전하는 것으로 예산 책정
        if oilMin > oil_lst[i]:
            oilMin = oil_lst[i]
        res += (oilMin * path_lst[i])
    
    return res

if __name__ == "__main__":
    size = int(sys.stdin.readline().rstrip())
    path_lst = list(map(int, sys.stdin.readline().split()))
    oil_lst = list(map(int, sys.stdin.readline().split()))

    print(solve())
