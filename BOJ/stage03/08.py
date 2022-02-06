size = int(input())
n_list = []
m_list = []
res = []

for i in range(1, size + 1) :
    n, m = map(int, input().split())
    n_list.append(n)
    m_list.append(m)
    res.append(n + m)

for i in range(0, size) :
    sen = "Case #{}: {} + {} = {}".format(i + 1, n_list[i], m_list[i], res[i])
    print(sen)