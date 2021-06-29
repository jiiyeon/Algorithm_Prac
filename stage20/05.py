#조건 : 곱셈정리와 페르마의 소정리를 활용함
## 페르마의 소정리 : a ** (p - 1) ≡ 1 (mod p)

import sys

def     power(a, b):
    if b == 0:
        return 1

    else:

        #분배법칙 규칙 이용
        if b % 2 == 0:
            return (power(a, b // 2) ** 2) % div
        else:
            return (power(a, b // 2) ** 2 * a) % div

if __name__ == "__main__":

    N, K  = map(int, sys.stdin.readline().split())
    
    div = 1000000007

    #factorial을 미리 계산하여 나머지 산출
    fact_value = [1 for _ in range(N + 1)]
    for i in range(2, N + 1):
        fact_value[i] = fact_value[i - 1] * i % div
    
    # nCk == n! / (n - k)! * k!
    A = fact_value[N]
    B = (fact_value[N - K]  * fact_value[K]) % div

    print((A % div) * (power(B, div - 2) % div) % div)
