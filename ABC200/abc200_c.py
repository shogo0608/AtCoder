# 2021/08/28

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

modulo_cnt = defaultdict(int)
for a in A:
    modulo_cnt[a%200] += 1
ans = 0
for v in modulo_cnt.values():
    ans += v * (v-1) // 2

print(ans)