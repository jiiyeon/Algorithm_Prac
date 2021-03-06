#조건 : n == 3 ** i 일 때, 가운데를 제외한 자리에 n == 3 ** (i - 1)의 배열이 들어감
import sys

def     ft_star(int) :
    #함수 안에서도 전역변수 값을 수정하기 위해서 Global문 사용
    global Board
    
    #가장 아래 부분에서 return
    if (int == 3) :
        Board[0][:3] = Board[2][:3] = ["*"] * 3
        Board[1][:3] = ["*", " ", "*"]
        return

    #반복할 부분
    div_3 = int // 3
    ft_star(int // 3)
    i = 0
    while (i < int) :

        j = 0
        while (j < int) :
            if (i != div_3 or j != div_3) :
                
                r = 0
                while (r < div_3) :
                    Board[i + r][j : j + div_3] = Board[r][:div_3]
                    r += 1
            j += div_3
        i += div_3

N = int(sys.stdin.readline())
Board = [[" " for _ in range(N)] for _ in range(N)]
ft_star(N)

i = 0
while (i < N) :
    
    j = 0
    while (j < N) :
        print(Board[i][j], end="")
        j += 1
    print()
    i += 1