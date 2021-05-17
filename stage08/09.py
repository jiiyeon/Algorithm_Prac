size = int(input())

def     distance(X, Y) :
    
    cnt = 0
    
    #시작점과 종료점 이동량은 고정됨
    X += 1
    cnt += 1
    if (X < Y) :
        Y -= 1
        cnt += 1

    #처음부터 중간지점까지는 이동량이 1씩 증가하고 중간부터 끝까지는 이동량이 1씩 감소함
    s = 1
    mid = (X + Y) // 2
    while (X < Y) :
        if (X + s >= Y) :
            break
        
        if (X <= mid) :
            s += 1
        else :
            s -= 1

        X += s
        cnt += 1
    if (X != Y) :
        cnt +=1

    return(cnt)

i = 0
cnt_lst = []
while (i < size) :
    A, B = map(int, input().split())
    cnt_lst.append(distance(A, B))
    i += 1

i = 0
while (i < size) :
    print(cnt_lst[i])
    i += 1