A = int(input())
B = int(input())
C = int(input())
mul = A * B * C
mul_int = []

while (mul != 0) :
    mul_int.append(mul % 10)
    mul //= 10

i = 0
mul_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while (mul_int[i]) :

    index = mul_count.index(mul_int[i])
    mul_count[index] += 1
    i += 1

i = 0
while (i < 10) :
    print(mul_count[i])