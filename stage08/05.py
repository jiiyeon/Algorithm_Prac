# 조건1 : H층의 호텔의 N번째 손님에 대해서, N % H == 배정할 방의 층수, N // H + 1 == 배정할 방의 칸수
# 조건2 : 단, N % H == 0 일 경우 H층에 배정함

size = int(input())

def     room_num(H, N) :
    
    front = N % H
    end = ""
    if (front == 0) :
        front = str(H)
        end = N // H
    else :
        front = str(front)
        end = N // H + 1
    
    if (end >= 10) :
        end = str(end)
    else :
        end = "0" + str(end)
    
    res = front + end
    return(res)

i = 0
room_batch = []
while (i < size) :
    H, W, N = map(int, input().split())
    room_batch.append(room_num(H, N))
    i += 1

i = 0
while (i < size) :
    print(room_batch[i])
    i += 1