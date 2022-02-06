#조건 : 피보나치수열을 동적계획법으로 해결
# 피보나치 수열(fibo)은 재귀로 구현했을 때 fibo(0), fibo(1)로 분해될 때까지 내려가므로
# 만약 fibo(0)과 fibo(1)이 몇 번 등장하는지 규칙을 찾을 수 있다면 1번의 연산으로 피보나치수를 구할 수 있음

#fibo(0)과 fibo(1)의 등장횟수도 피보나치수열을 만족함
# 조건1 : n번째 수에서 0의 등장횟수 == (n - 1)번째 수에서 0의 등장횟수 + (n - 2)번째 수에서 0의 등장횟수
# 조건2 : n번째 수에서 1의 등장횟수 == (n - 1)번째 수에서 0의 등장횟수 + (n - 2)번째 수에서 0의 등장횟수
# N이 40이하의 자연수라고 주어졌으므로 zero_cnt, one_cnt의 list 생성 후 index로 호출하여 출력

import sys

zero_cnt = [1, 0]
one_cnt = [0, 1]

for i in range(2, 41):
    zero_cnt.append(zero_cnt[i - 1] + zero_cnt[i - 2])
    one_cnt.append(one_cnt[i - 1] + one_cnt[i - 2])

size = int(sys.stdin.readline().rstrip())
i = 0
while i < size:
    idx = int(sys.stdin.readline().rstrip())
    print(zero_cnt[idx], one_cnt[idx])
    i += 1
