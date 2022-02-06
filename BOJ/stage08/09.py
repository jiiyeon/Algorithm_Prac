import math

size = int(input())
i = 0
while (i < size) :

    x, y = map(int, input().split())
    diff = int(y - x)
    if (diff <= 3) :
        print(diff)
    else:

        n = int(math.sqrt(diff))
        if (diff == pow(n, 2)) :
            print(2 * n - 1)
        elif (pow(n, 2) < diff <= pow(n, 2) + n) :
            print(2 * n)
        else:
            print(2 * n + 1)
    i += 1