import math

r = int(input())

#유클리드 기하학에서 원의 넓이
print(round((r ** 2) * math.pi, 4))

#택시 기하학에서 원의 넓이(마름모넓이) == (2 * r) * (2 * r) * 1/2
print(round((2 * (r ** 2)), 4))