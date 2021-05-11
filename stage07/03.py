str_lst = list(input())

i = 97
while (i <= 122) :
    if (chr(i) in str_lst) :

        j = 0
        while (j < len(str_lst)) :
            if (chr(i) == str_lst[j]) :
                print(j, end=" ")
                break
            j += 1
    else :
        print("-1", end=" ")
    i += 1 