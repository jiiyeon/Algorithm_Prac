def     div_count(int) :

    i = 0
    sum = int
    while (int != 0) :
        sum += int % 10
        int //= 10
        i += 1
    
    return (sum)

i = 0
int = 1
decom_lst = []
while (int <= 10000) :
    decom_lst.append(div_count(int))
    int += 1
decom_lst = set(decom_lst)

i = 0
int = 1
while (int <= 10000) :
    if (int not in decom_lst) :
        print(int)
    int += 1