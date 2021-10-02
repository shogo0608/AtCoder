from collections import defaultdict

N = int(input())
people_cnt = defaultdict(int)
for _ in range(N):
    A, B = map(int, input().split())
    for d in range(A, A + B):
        people_cnt[d] += 1
day_cnt = defaultdict(int)
for v in people_cnt.values():
    day_cnt[v] += 1

for i in range(1, N + 1):
    print(day_cnt[i], end=" ")