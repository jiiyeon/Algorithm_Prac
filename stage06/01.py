a = list(map(int, input().split()))

def     solve(a) :
    n = len(a)

    i = 0
    sum = 0
    while (i < n) :
        sum += a[i]
        i += 1

    return(sum)

print(solve(a))