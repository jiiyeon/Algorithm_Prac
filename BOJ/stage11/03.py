import sys

def     ft_cnt(size, row) :

    global  data

    height = row[0]
    weight = row[1]

    i = 0
    cnt = 1
    while (i < size) :
        if ((height < data[i][0]) and (weight < data[i][1])) :
            cnt += 1
        i += 1
    
    return (cnt)

size = int(sys.stdin.readline().strip())
i = 0
data = []
while (i < size) :
    w, h = map(int, sys.stdin.readline().split())
    data.append([w, h])
    i += 1

i = 0
while (i < size) :
    print(ft_cnt(size, data[i]))
    i += 1