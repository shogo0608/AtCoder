# 2021/09/12

from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for pattern in permutations(range(1, N)):
    cnt = T[0][pattern[0]]
    for i in range(N-2):
        cnt += T[pattern[i]][pattern[i+1]]
    cnt += T[pattern[-1]][0]
    if cnt == K:
        ans += 1

print(ans)