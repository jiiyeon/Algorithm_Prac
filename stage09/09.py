import sys

while (1) :
    a, b, c = map(int, sys.stdin.readline().split())

    if (a == 0 or b == 0 or c == 0) :
        break

    hypo = max(a, b, c)
    others = 0
    
    for i in [a, b, c] :
        if (i != hypo) :
            others += i ** 2
    
    if (hypo ** 2 == others) :
        print("right")
    else :
        print("wrong")