N = int(input())

def     group_check(char) :

    alpha_lst = []
    i = 97
    while (i < 123 ) :
        alpha_lst.append(chr(i))
        i += 1

    sen = list(char)

    i = 0
    j = 0
    while (j < 26) :
        if (sen[i] == alpha_lst[j]) :
            sen[i] = "*"
            i += 1
            if (i == len(sen)) :
                break
            elif (sen[i] != alpha_lst[j]) :
                alpha_lst[j] = "0"
                j = 0
        else :
            j += 1

    r = 0
    res = 1
    while (r < len(sen)) :
        if (sen[r] != "*") :
            res = 0
            break
        r += 1
    
    return(res)

num = 0
cnt = 0
while (num < N) :
    
    char = input()
    if (group_check(char) == 1) :
        cnt += 1
    num += 1

print(cnt)