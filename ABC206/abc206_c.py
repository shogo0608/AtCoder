# 2021/08/25

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt_dict = defaultdict(int)
for a in A:
    cnt_dict[a] += 1
ans = N * (N - 1) // 2
for v in cnt_dict.values():
    if v > 1:
        ans -= v * (v - 1) // 2

print(ans)