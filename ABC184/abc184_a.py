# 2021/09/17

A = [list(map(int, input().split())) for _ in range(2)]

print(A[0][0]*A[1][1] - A[0][1]*A[1][0])