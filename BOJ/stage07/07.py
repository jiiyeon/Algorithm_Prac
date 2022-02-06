A, B = input().split()

a = ""
b = ""
i = 0
while (i < 3) :
    a += A[2 - i]
    b += B[2 - i]
    i += 1

a = int(a)
b = int(b)
if (a > b) :
    print(a)
else :
    print(b)