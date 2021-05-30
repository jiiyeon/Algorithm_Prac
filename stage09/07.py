x, y, w, h = map(int,input().split())

#조건 : 0부터 x까지의 거리와 x부터 w까지의 거리를 비교하여 작은 값 채택 (y도 동일한 조건 적용)
diff_x = min(x, abs(x - w))
diff_y = min(y, abs(y - h))

if (diff_x >= diff_y) :
    print(diff_y)
else :
    print(diff_x)