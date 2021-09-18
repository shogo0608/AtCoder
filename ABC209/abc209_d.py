# 2021/09/15

from collections import defaultdict

def calc_distance(tree: dict, a: int, b: int) -> int:
    """Return distance from a to b
    """
    pass # ToDo

N, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
queries = [tuple(map(int, input().split())) for _ in range(Q)]

for c, d in queries:
    distance = calc_distance(tree, c, d)
    print("Road" if distance % 2 else "Town")