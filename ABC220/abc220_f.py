from collections import defaultdict

N = int(input())
G = defaultdict(list)
P = {}
for _ in range(N):
    u, v = map(int, input().split())
    G[u].append(v)
    P[v] = u
