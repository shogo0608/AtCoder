# 2021/08/26

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [B[c-1] for c in C]
A_cnt = defaultdict(int)
B_cnt = defaultdict(int)
for i in range(N):
    A_cnt[A[i]] += 1
    B_cnt[B[i]] += 1
ans = 0
for v in set(A) & set(B):
    ans += A_cnt[v] * B_cnt[v]

print(ans)