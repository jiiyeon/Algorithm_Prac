#조건1 : 각 사람들이 현금을 인출하기 위해 소요한 시간 = 앞 사람들의 처리시간 + 자신의 처리시간
#조건2 : 기계가 1대이므로 대기시간이 누적됨
# 즉 앞사람들의 처리시간이 짧아야 누적되는 값이 작아질 수 있으므로 처리시간이 짧은 사람부터 업무를 보도록 정리

import sys

def     solve(arr):
    total = 0
    wait = 0

    #total은 모든 사람이 소요한 시간의 합
    # 따라서 각 사람이 자신의 차례가 되었을때, 자신의 차례가 되기까지 걸린 시간(wait)과 자신의 업무시간(time)을 total에 추가함
    for time in arr:
        total += (wait + time)
        wait += time
    
    return total

#시작함수
if __name__ == "__main__":

    size = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = sorted(arr)

    print(solve(arr))
