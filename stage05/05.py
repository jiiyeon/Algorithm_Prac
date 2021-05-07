size = int(input())
score = list(map(float, input().split()))

i = 0
Max = score[0]
while (i < size) :
    if (Max < score[i]) :
        Max = score[i]
    i += 1

i = 0
sum = 0
while (i < size) :
    score[i] = score[i] / Max * 100
    sum += score[i]
    i += 1

print(sum / size)