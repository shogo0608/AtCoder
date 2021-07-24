import math

P = int(input())

num_coins = 0
for i in reversed(range(1, 11)):
    num = P // math.factorial(i)
    num_coins += num
    P -= num * math.factorial(i)

print(num_coins)