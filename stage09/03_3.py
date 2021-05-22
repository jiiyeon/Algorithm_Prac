N = int(input())

i = 2
while (1) :
    if (N == 1) :
        break
    while (N % i == 0) :
        print(i)
        N //= i
    i += 1