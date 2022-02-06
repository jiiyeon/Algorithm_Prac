# 규칙1 : [1/1], [1/2, 2/1], [3/1, 2/2, 1/3]... 으로 그룹번호가 그룹의 원소의 개수
# 규칙2 : 홀수번째 그룹은 첫번째 항이 N/1이고 짝수번째 그룹은 첫번째 항이 1/N

N = int(input())

def    find_group(int) :

    i = 1
    sum = 0
    while (1) :
        sum += i
        if (sum >= int) :
            break
        i += 1
    return([i, sum - i])

idx = find_group(N)[0]
mod = N - find_group(N)[1]
if (idx % 2 == 1) :
    print(idx - mod + 1, "/", mod, sep="")
else :
    print(mod, "/", idx - mod + 1, sep="")