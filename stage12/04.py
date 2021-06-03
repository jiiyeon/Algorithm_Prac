import sys

def     ft_sum(list):

    return sum(list) // len(list)

def     ft_mid(list):
    sort_lst = sorted(list)
    N = len(sort_lst) // 2

    return sort_lst[N]

def     ft_freq(list):
    freq_dict = {i : 0 for i in set(list)}
    i = 0
    while i < len(list):
        freq_dict[list[i]] += 1
        i += 1

    MAX = 0
    if len(list) == 1:
        MAX = list[0]
    else :
        MAX = max(freq_dict.values())
    
    return freq_dict[MAX]

def     ft_range(list):
    sort_lst = sorted(list)
    return sort_lst[-1] - sort_lst[0]

size = int(sys.stdin.readline())
num_lst = []
i = 0
while i < size:
    num_lst.append(int(sys.stdin.readline().strip()))
    i += 1

print(ft_sum(num_lst))
print(ft_mid(num_lst))
print(ft_freq(num_lst))
print(ft_range(num_lst))
