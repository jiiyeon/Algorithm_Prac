N = int(input())

def    find_group(int) :

    i = 1
    sum = 0
    while (1) :
        sum += i
        if (sum >= int) :
            break
        i += 1
    return([i, sum - i])

idx = find_group(N)[0]
mod = N - find_group(N)[1]
if (idx % 2 == 1) :
    print(idx - mod + 1, "/", mod, sep="")
else :
    print(mod, "/", idx - mod + 1, sep="")