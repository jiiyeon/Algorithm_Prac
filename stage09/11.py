#조건1 : 류재명이 있을 수 있는 좌표의 수 == 조규현의 원(조규현 시점에서 류재명 좌표후보의 집합)과 백승환의 원이 만나는 교점의 개수
# 두 원의 교점의 수는 중점거리의 연산을 통해서 알 수 있음

import sys
import math

size = int(sys.stdin.readline())

i = 0
while (i < size) :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if (d == 0 and r1 == r2) :
        print(-1)
    elif (d == r1 + r2) :
        print(1)
    elif (abs(r1 - r2) <= d and d < r1 + r2) :
        print(2)
    else :
        print(0)
    
    i += 1