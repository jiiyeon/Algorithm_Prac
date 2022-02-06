num = int(input())

if (num < 10) :
    num *= 10

mod1 = num % 20
mid = num // 10 + mod1
mod2 = mid % 10

i = 1
while (mod1 * 10 + mod2 != num) :
    mid = mod1 + mod2
    mod1 = mod2
    mod2 = mid % 10
    i += 1

print(i)