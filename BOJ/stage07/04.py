N = int(input())

i = 0
sen_lst = []
while (i < N) :
    sen_lst.append(input())
    i += 1

def     word_append(lst) :
    N = int(lst[0])
    alphanu = list(r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:")

    i = 2
    res = ""
    while (i < len(lst)) :
        if (lst[i] in alphanu) :
            res += lst[i] * N
        i += 1
    
    return(res)

i = 0
while (i < N) :
    print(word_append(sen_lst[i]), end="")
    print("")
    i += 1