# 2021/09/09

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        gradient = (P[j][1] - P[i][1]) / (P[j][0] - P[i][0])
        if gradient >= -1 and gradient <= 1:
            cnt += 1

print(cnt)