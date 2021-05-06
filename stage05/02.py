num = []

i = 0
Max = 0
while (i < 9) :
    num.append(int(input()))

    if (num[i] > Max) :
        Max = num[i]
    i += 1

index = num.index(Max)
print(num[index], index)