# 2021/09/14

from collections import defaultdict

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

X = defaultdict(int)
Y = defaultdict(int)
for x, y in P:
    X[x] += 1
    Y[y] += 1
flag = False
for v in X.values():
    if v > 2:
        flag = True
for v in Y.values():
    if v > 2:
        flag = True

print("Yes" if flag else "No")