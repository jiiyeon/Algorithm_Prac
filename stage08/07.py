#조건1 : 더 적은 수의 주머니를 가져가고 싶으므로 N을 5kg로 나눈 나머지에 대해서 3kg으로 나눔
#조건2 : mod = N % 5에 따라서 5kg 주머니의 개수를 줄여야함
# 1) 0 or 3 : PASS
# 2) 1 or 4 : 5kg 주머니를 1개 줄이면 3으로 나누어떨어짐
# 3) 2 : 5kg 주머니를 2개 줄이면 3으로 나누어떨어짐
#조건3 : 만약 나누어 떨어지지 않는다면 -1 출력

N = int(input())

cnt = 0
while (N >= 0) :
    if (N % 5 == 0) :
        cnt += (N // 5)
        break
    elif (N == (1 or 2 or 4)) :
        cnt = -1
        break
    N -= 3
    cnt += 1
print(cnt)