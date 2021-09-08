# 2021/09/08

from math import factorial

L = int(input())

print(factorial(L-1) // factorial(L-12) // factorial(11))