#카운팅 정렬 : 배열을 먼저 선언하여 입력값의 위치에 빈도를 저장함
# 이후 배열에서 존재하는 수를 빈도만큼 출력함

import sys

size = int(sys.stdin.readline())
num_dict = {i : 0 for i in range(10001)}

i = 0
while i < size:
    num = int(sys.stdin.readline())
    num_dict[num] += 1
    i += 1

for i in num_dict:
    cnt = num_dict[i]
    while cnt > 0:
        print(i)
        cnt -= 1
