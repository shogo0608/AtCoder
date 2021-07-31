# 2021/07/31

from collections import defaultdict

N, K = map(int, input().split())
friends = defaultdict(int)
for _ in range(N):
    A, B = map(int, input().split())
    friends[A] += B

for i in sorted(friends.keys()):
    if K >= i:
        K += friends[i]
    else:
        break

print(K)