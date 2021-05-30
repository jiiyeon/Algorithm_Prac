x, y, w, h = map(int,input().split())

diff_x = min(x, abs(x - w))
diff_y = min(y, abs(y - h))

if (diff_x >= diff_y) :
    print(diff_y)
else :
    print(diff_x)