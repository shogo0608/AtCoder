# 2021/09/21

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num_idx = defaultdict(list)
for i in range(N):
    num_idx[A[i]].append(i)
ans = 0
for i in range(N//2):
    a, b = A[i], A[N-i-1]
    if a != b:
        changed_list = num_idx[b]
        for idx in changed_list:
            A[idx] = a
        num_idx[a] += num_idx[b]
        num_idx[b] = []
        ans += 1

print(ans)