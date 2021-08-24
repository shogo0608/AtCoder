# 2021/08/24

N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
balls = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for i in range(2**K):
    dishes = set()
    for j in range(K):
        dishes.add(balls[j][(i >> j) & 1])
    cnt = 0
    for j in range(M):
        if conditions[j][0] in dishes and conditions[j][1] in dishes:
            cnt += 1
    ans = max(ans, cnt)

print(ans)