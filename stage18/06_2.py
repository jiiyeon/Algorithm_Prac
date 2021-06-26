import sys

size = int(sys.stdin.readline().rstrip())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(size)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
#배열을 print할 때 *을 붙이면 공백기준으로 원소들만 출력함
print(*answer)
 