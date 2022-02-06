A = int(input())
B = int(input())
C = int(input())
mul = A * B * C
mul_int = []

while (mul != 0) :
    mul_int.append(mul % 10)
    mul //= 10

j = 0
mul_count = []
while (j < 10) :

    i = 0
    num = 0
    while (i < len(mul_int)) :
        if (mul_int[i] == j) :
            num += 1
        i += 1
    mul_count.append(num)
    j += 1

i = 0
while (i < 10) :
    print(mul_count[i])
    i += 1