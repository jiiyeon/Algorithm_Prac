import sys


def ft_sum(list):

    # 소수 첫째자리에서 반올림. //을 쓰면 몫만 남기고 버림
    return round(sum(list) / len(list))


def ft_mid(list):
    sort_lst = sorted(list)
    N = len(sort_lst) // 2

    return sort_lst[N]


def ft_freq(list):
    freq_dict = {i: 0 for i in set(list)}
    i = 0
    while i < len(list):
        freq_dict[list[i]] += 1
        i += 1

    MAX = max(freq_dict.values())
    max_lst = [x for x in freq_dict if freq_dict[x] == MAX]
    max_lst = sorted(max_lst)

    if len(max_lst) == 1:
        res = max_lst[0]
    else:
        res = max_lst[1]

    return res


def ft_range(list):
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
