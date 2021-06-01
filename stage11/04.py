#조건1 : 8*8 바둑판을 자른다 == [a:a + 8][:8]범위로 모든 경우를 검사함
#조건2 : 시작점(첫줄 제일 왼쪽 칸)이 W인지 B인지에 따라 칠하는 개수가 다름

import sys

row, col = map(int, sys.stdin.readline().split())

i = 0
data = []
while (i < row) :
    data.append(sys.stdin.readline().strip())
    i += 1
print(data[0][1])

r = 0
cnt_lst = []
while (r < (row - 7)) :

    s = 0
    while (s < (col - 7)) :
        cnt_w = 0
        cnt_b = 0

        #8 * 8 바둑판에 대해서 시작점이 W일때와 B일 때를 모두 검사
        r_cycle = r
        while (r_cycle < (r_cycle + 8)) :

            s_cycle = s
            while (s_cycle < (s_cycle + 8)) :

                #바둑판의 같은 column에서 위아래의 값이 달라야함
                if (r_cycle + s_cycle % 2 == 0) :

                    #W로 시작할때
                    if (data[r_cycle][s_cycle] != "W") :
                        cnt_w += 1
                        print(data[r_cycle][s_cycle])
                    #B로 시작할때
                    elif (data[r_cycle][s_cycle] != "B") :
                        cnt_b += 1
                else :
                    if (data[r_cycle][s_cycle] != "B") :
                        cnt_b += 1
                    elif (data[r_cycle][s_cycle] != "W") :
                        cnt_w += 1
                s_cycle +=1
            r_cycle +=1

        cnt_lst.append(cnt_w)
        cnt_lst.append(cnt_b)

        s += 1
    r += 1

print(min(cnt_lst))