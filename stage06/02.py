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
while (int <= 10000) :
    print(div_count(int))
    int = div_count(int)