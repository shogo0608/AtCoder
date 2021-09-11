# 2021/09/06

N = int(input())
A, B = (list(map(int, input().split())) for _ in range(2))

dot = 0
for i in range(N):
    dot += A[i] * B[i]

print("Yes" if dot==0 else "No")