import sys

size = int(input())

i = 0
ox_list = []
while (i < size) :
    ox_list.append(sys.stdin.readline())
    i += 1

def ox_count(string) :
    n = len(string)
    str_list = list(string)

    i = 0
    j = 0
    sum = 0
    while (i < n) :
        if (str_list[i] == "O") :
            j += 1
            sum += j
        else :
            j = 0
        i += 1

    return(sum)

i = 0
while (i < size) :
    print(ox_count(ox_list[i]))
    i += 1