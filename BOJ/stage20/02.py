#조건 : image data 처리, 쿼드트리

import sys

def     solve(x, y, size):
    
    res = []
    check = image[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):

            #현재 범위에서 (x, y)값과 다른 값이 하나라도 있으면 재귀로 4분할 호출
            if image[i][j] != check:
                res.append("(")

                #1사분면
                res.extend(solve(x, y, size // 2))
                #2사분면
                res.extend(solve(x, y + size // 2, size // 2))
                #3사분면
                res.extend(solve(x + size // 2, y, size // 2))
                #4사분면
                res.extend(solve(x + size // 2, y + size // 2, size // 2))

                res.append(")")
                return res

    return str(image[x][y])

#시작함수
if __name__ == "__main__":

    size = int(sys.stdin.readline().rstrip())
    image = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(size)]
    
    print("".join(solve(0, 0, size)))
