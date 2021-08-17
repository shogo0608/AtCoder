# 2021/08/17

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

A_dict = defaultdict(int)
for a in A:
    A_dict[a] += 1
ans = 0
for i in A_dict.keys():
    for j in A_dict.keys():
        ans += ((i - j) ** 2) * A_dict[i] * A_dict[j]

print(ans//2)