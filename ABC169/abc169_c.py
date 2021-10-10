# 2021/10/10

A, B = input().split()
A = int(A)

print(A * int(B[:-3] + B[-2] + B[-1]) // 100)