size = int(input())
num_list = list(input())

i = 0
sum = 0
while (i < size) :
    num_list[i] = int(num_list[i])
    sum += num_list[i]
    i += 1

print(sum)