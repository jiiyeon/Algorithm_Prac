div = []

i = 0
while (i < 10) :
    num = int(input())
    num %= 42
    div.append(num)
    i += 1

div = set(div)
print(len(div))