# 2021/08/02

A = list(map(int, input().split()))

A.sort()
if A[1] - A[0] == A[2] - A[1]:
    print("Yes")
else:
    print("No")