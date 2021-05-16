# 시간제한이 관건. while 문으로 하루씩 이동하는 것을 생각했으나, 곱셈과 나머지를 이용하여 수정

A, B, V = map(int, input().split())

i = A - B
if ((V - B) % i == 0) :
    cnt = (V - B) // i 
else :
    cnt = (V - B) // i + 1

print(cnt)