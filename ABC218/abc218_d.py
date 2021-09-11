from collections import defaultdict
from math import factorial

N = int(input())
y_dict = defaultdict(set)
for _ in range(N):
    x, y = map(int, input().split())
    y_dict[x].add(y)

ans = 0
for x in y_dict.keys():
    for xx in y_dict.keys():
        if x == xx:
            continue
        num_y = len(y_dict[x] & y_dict[xx])
        ans += factorial(num_y) // factorial(num_y-2) // factorial(2) if num_y > 1 else 0

print(ans//2)