sen_lst = list(input().upper())
sen_unique = list(set(sen_lst))

i = 0
cnt = []
while (i < len(sen_unique)) :
    cnt.append(sen_lst.count(sen_unique[i]))
    i += 1

j = 0
max_idx = []
while (j < len(cnt)) :
    if (cnt[j] == max(cnt)) :
        max_idx.append(j)
        idx = j
    j += 1


if (len(max_idx) != 1) :
    print("?")
else :
    print(sen_unique[idx])