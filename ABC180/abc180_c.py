# 2021/09/23

from collections import deque

N = int(input())

lower, upper = [], []
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        lower.append(i)
        if N//i != i:
            upper.append(N//i)

ans = lower + list(reversed(upper))
print(*ans, sep="\n")