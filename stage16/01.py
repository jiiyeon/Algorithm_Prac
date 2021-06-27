#조건 : 가장 적은 동전을 사용하여 금액을 만들 것
# 큰 금액의 동전부터 사용함

import sys

N, value = map(int, sys.stdin.readline().split())
type_lst = []
for _ in range(N):
    type_lst.append(int(sys.stdin.readline().rstrip()))

i = N - 1
diff = value
cnt = 0
while 1:
    if diff >= type_lst[i]:
        diff -= type_lst[i]
        cnt += 1

        if diff == 0:
            break
    
    else:
        i -= 1

print(cnt)
