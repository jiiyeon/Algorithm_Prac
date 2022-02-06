#조건 : 입력받은 수들 중 자신보다 작은 수의 개수 == 정렬했을 때 최초의 index
# index함수에서 list안에서 값을 가지는 최초의 index를 반환함
#조건2 : index함수를 매번 수행하면 시간초과 -> 1번만 수행하여 값을 저장하여 불러옴

import sys

size = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

sort_data = sorted(set(data))
sort_index = {sort_data[i] : i for i in range(len(sort_data))}

i = 0
while i < len(data):
    print(sort_index[data[i]], end=" ")
    i += 1
