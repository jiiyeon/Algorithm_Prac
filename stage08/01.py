A, B, C = map(int, input().split())

ch_point = 0
if (C <= B) :
    ch_point = 1
else :
    ch_point = A // (C - B) + 1
print(ch_point)