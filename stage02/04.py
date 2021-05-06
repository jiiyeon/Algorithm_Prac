H, M = map(int, input().split())

if (45 <= M and M <= 59) :
    M -= 45
else :
    M += 15
    H--
    if (H < 0) :
        H += 24
print(H, M)
