from collections import deque


def bfs(node, que, depth, G, N, counts):
    for n in G[node]:
        if n == N-1:
            counts += 1
        que.append(n)
        depth[n] = depth[node] + 1
    if len(que) == 0:
        return counts
    if N-1 in depth and depth[node] >= depth[N-1]:
        return counts
    next_node = que.popleft()
    return bfs(next_node, que, depth, G, N, counts)


N, M = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

que = deque()
depth = {0: 0}
ans = bfs(0, que, depth, G, N, 0)

print(ans % (10**9+7))