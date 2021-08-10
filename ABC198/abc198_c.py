# 2021/08/10

from math import sqrt, ceil

R, X, Y = map(int, input().split())

print(ceil(sqrt((X*X + Y*Y) / (R*R))))