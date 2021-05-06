size = int(input())

for i in range(1, size + 1) :
    space = " " * (size - i)
    star = "*" * i
    print(space + star)