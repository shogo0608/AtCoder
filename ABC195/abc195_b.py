# 2021/08/16

from math import ceil

A, B, W = map(int, input().split())

W *= 1000

flag = False
for i in range(B, A-1, -1):
    if W % i == 0:
        print(W // i, end=" ")
        break
for i in range(A, B+1):
    if W % i == 0:
        print(W // i)
        flag = True
        break

if not flag:
    print("UNSATISFIABLE")