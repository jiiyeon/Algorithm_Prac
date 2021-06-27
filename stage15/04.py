#조건 : 6번째 수부터 s[i] = s[i - 1] + s[i - 5]

import sys

size = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(size)]
s = [1, 1, 1, 2, 2]

for i in range(5, max(arr)):
    s.append(s[i - 1] + s[i - 5])

for idx in arr:
    print(s[idx - 1])
