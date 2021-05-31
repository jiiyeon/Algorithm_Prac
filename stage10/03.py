#조건 : n == 3 ** i 일 때, 가운데를 제외한 자리에 n == 3 ** (i - 1)의 배열이 들어감
def     ft_star(int) :
    #함수 안에서도 전역변수 값을 수정하기 위해서 Global문 사용
    global Board
    
    #가장 아래 부분에서 return
    if (int == 3) :
        Board[0][:3] = Board[2][:3] = ["*", "*", "*"]
        Board[1][:3] = ["*", " ", "*"]
        return

    #반복할 부분
    a = int // 3
    ft_star(int // 3)
    i = 0
    while (i < 3) :

        j = 0
        while (j < 3) :
            if (i == 1 and j == 1) :
                continue
            r = 0
            while (r < a) :
                Board[a * i + r][a * j : a * (j + 1)] = Board[r][:a]
                r += 1
            j += 1
        i += 1

N = int(input())
Board = [[" " for i in range(N)] for i in range(N)]
ft_star(N)

i = 0
while (i < N) :
    
    j = 0
    while (j < N) :
        print(Board[i][j])
        j += 1
    i += 1