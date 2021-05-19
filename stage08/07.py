#조건1 : 5kg의 주머니를 많이 가져가고 싶으므로, 무게가 5kg의 배수가 될 때까지만 3kg 주머니를 가져감 
#조건2 : 만약 나누어 떨어지지 않는다면 -1 출력

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