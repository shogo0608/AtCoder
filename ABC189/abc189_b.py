# 2021/09/02

N, X = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

i = 0
cnt = 0
ans = -1
while i < N:
    cnt += A[i][0] * A[i][1]
    if cnt > X * 100:
        ans = i + 1
        break
    i += 1

print(ans)