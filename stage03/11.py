size, Max = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(0, size) :
    if (num_list[i] < Max) :
        print(num_list[i], end=" ")