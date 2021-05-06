size = int(input())
num = list(map(int, input().split()))

Min = num[0]
Max = num[0]
i = 0
while (i < size) :
    if (num[i] < Min) :
        Min = num[i]
    elif (num[i] > Max) :
        Max = num[i]
    i += 1

print(Min, Max)