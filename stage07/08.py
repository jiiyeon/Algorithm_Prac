dial_lst = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
key = input().lower()

i = 0
sum = 0
while (i < len(key)) :
    
    j = 0
    while (j < len(dial_lst)) :
        if (key[i] in dial_lst[j]) :
            sum += (j + 3)
            break
        j += 1
    i += 1

print(sum)