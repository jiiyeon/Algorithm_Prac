#조건 : 회의가 가장 많이 열릴 수 있도록 일정 구성 (i번째의 회의시간이 짧고, i번째에서 i + 1 번째로 넘어가는 간격이 짧아야함)
# 회의가 빨리 끝나는 기준으로 선택하면, 남은 시간이 더 길어지므로 고려할 수 있는 회의 수가 늘어남
# 따라서 회의시각을 key1 : 회의 종료 시각, key2 : 회의 시작 시각으로 정렬하여 순서 그대로 cnt

import sys

def     solve(table):
    cnt = 0
    start = 0

    #정렬된 회의 시간표 순서쌍(start, end)에서
    for time in table:

        #만약 time이 가능한 시작시점과 같이(또는 늦게) 시작한다면 time을 포함하고
        # 회의 시작 가능한 시각을 time이 끝나는 시각으로 변경함
        if time[0] >= start:
            start = time[1]
            cnt += 1
    
    return cnt

#시작함수
if __name__ == "__main__":
    size = int(sys.stdin.readline().rstrip())
    table = []

    for i in range(size):
        start, end = map(int, sys.stdin.readline().split())
        table.append((start, end))
    
    #key1 : 종료시각, key2 : 시작시각
    # sorted에서 key가 여러 개 사용될 경우 tuple 사용
    table = sorted(table, key=lambda x: (x[1], x[0]))
    print(solve(table))
