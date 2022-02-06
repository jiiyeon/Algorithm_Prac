num1 = int(input())
num2 = int(input())

mul1 = num1 * ((num2 % 100) % 10)
mul2 = num2 * ((num2 % 100) // 10)
mul3 = num1 * (num2 // 100)
res = num1 * num2

print(mul1, mul2, mul3, res, sep='\n')
