#조건 : 결과값이 최소값이 되도록 ( )로 묶어서 계산함
# "-"에서 다음 "-"를 만날 때까지 입력값을 하나의 원소로 묶음

import sys

sen = sys.stdin.readline().split("-")
res = 0

#case1 : "-"부호 기준 앞부분
for item01 in sen[0].split("+"):
    res += int(item01)

#case2 : "-"부호 기준 뒷부분
# "-"가 여러번 등장했을 경우 sen[1:]에 해당하는 원소가 여러개일 수 있음
# 각 원소는 -( )형태이므로 "+"가 있는 경우 ( )안의 값을 꺼내서 각각 뺌
for item02 in sen[1:]:
    for sub_item02 in item02.split("+"):
        res -= int(sub_item02)

print(res)
