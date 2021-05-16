# 조건1 : 거주인원수열의 일반항 b[i] = sigma(a[i]) /* a(b의 한층아래수열의 일반항)[i] = i * (i + 1) / 2

size = int(input())

# 함수1 : 주어진 list에서 idx까지의 합을 구함
def     sub_sum(list, idx) :

    i = 0
    sum = 0
    while (i <= idx) :
        sum += list[i]
        i += 1
    
    return(sum)

# 함수2 : 층별 각 방의 거주인원 list를 하나의 원소로 건물 전체 인원의 list 생성 
def     cnt_people(floor, col) :

    total_lst = []
    element_lst = list(range(1, col + 1))

    i = 0
    while (i <= floor) :

        total_lst.append(element_lst)

        r = 0
        while (r < len(element_lst)) :
            element_lst[r] = sub_sum(element_lst, r)
            r += 1
        i +=1
    
    return(total_lst[floor][col - 1])


i = 0
while (i < size) :

    floor = int(input())
    col = int(input())

    print(cnt_people(floor, col))
    i += 1