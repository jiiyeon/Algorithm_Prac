size = int(input())
board = []

i = 0
while (i < size) :
    board.append(input())
    i += 1

def list_aver(string) :
    num_list = list(map(int, string.split()))
    N = num_list[0]

    i = 1
    sum = 0
    while (i < N + 1) :
        sum += num_list[i]
        i += 1
    aver = sum / N

    i = 1
    j = 0
    while (i < N + 1) :
        if (num_list[i] > aver) :
            j += 1
        i += 1
    
    return(j / N * 100)

i = 0
while (i < size) :
    print(format(list_aver(board[i]), ".3f"), "%", sep="")
    i += 1