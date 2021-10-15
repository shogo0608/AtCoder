# 2021/10/15

N, D = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    if P[i][0] ** 2 + P[i][1] ** 2 <= D ** 2:
        ans += 1

print(ans)