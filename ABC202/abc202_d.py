# 2021/09/28

from itertools import permutations

A, B, K = map(int, input().split())

print("".join(sorted(list(set(permutations("a" * A + "b" * B))))[K-1]))