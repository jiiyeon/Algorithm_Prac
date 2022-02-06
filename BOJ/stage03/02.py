size = int(input())
sum_list = []

for i in range(1, size + 1) :
    n, m = map(int, input().split())
    sum_list.append(n + m)

for i in range(0, size) :
    print(sum_list[i])