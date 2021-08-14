N = int(input())
G = [[] for _ in range(N)]
weight = [{} for _ in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    u = u - 1
    v = v - 1
    G[u].append(v)
    G[v].append(u)
    weight[u][v] = w
    weight[v][u] = w

dist = [[float('inf')]*N for _ in range(N)]
arrived = [False] * N

def dfs(s):
    global dist, arrived
    dist[s][s] = 0

    stack = [s]
    while stack:
        v = stack.pop()
        if arrived[v]:
            for i in range(len(dist[v])):
                dist[s][i] = min(dist[s][i], dist[s][v] + dist[s][i])
        for nv in G[v]:
            if dist[s][nv] > dist[s][v] + weight[v][nv]:
                stack.append(nv)
                dist[s][nv] = dist[s][v] + weight[v][nv]
    arrived[s] = True

for i in range(N):
    dfs(i)

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += dist[i][j]

print(ans)
