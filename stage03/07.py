size = int(input())
res = []

for i in range(1, size + 1) :
    n, m = map(int, input().split())
    res.append(n + m)

for i in range(0, size) :
    print("Case #", i + 1, ": ", res[i], sep="")