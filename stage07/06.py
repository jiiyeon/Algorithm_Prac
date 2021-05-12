word = input().split()

i = 0
word_lst = []
while (i < len(word)) :
    if (word[i] != "") :
        word_lst.append(word[i])
    i += 1

print(len(word_lst))