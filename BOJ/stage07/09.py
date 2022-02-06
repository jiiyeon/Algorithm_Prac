char_lst = ["c=","c-","dz=","d-","lj","nj","s=","z="]
sen = input()

i = 0
while (i < len(char_lst)) :
    sen = sen.replace(char_lst[i], "*")
    i += 1

print(len(sen))