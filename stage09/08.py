#순서쌍을 모두 받아서 x, y리스트로 나눠서 저장
i = 0
x_lst = []
y_lst = []
while (i < 3) :
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
    i += 1

#x_lst에 한번만 저장된 원소를 출력
if (x_lst[0] == x_lst[1]) :
    print(x_lst[2], end=" ")
elif (x_lst[0] != x_lst[1]) :
    if (x_lst[0] == x_lst[2]) :
        print(x_lst[1], end=" ")
    else :
        print(x_lst[0], end=" ")

#y_lst에 한번만 저장된 원소를 출력
if (y_lst[0] == y_lst[1]) :
    print(y_lst[2])
elif (y_lst[0]!= y_lst[1]) :
    if (y_lst[0] == y_lst[2]) :
        print(y_lst[1])
    else :
        print(y_lst[0])