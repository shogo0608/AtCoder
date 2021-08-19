# 2021/08/19

N = int(input())
ans = float('inf')
for _ in range(N):
    A, P, X = map(int, input().split())
    if X - A > 0:
        ans = min(ans, P)

if ans == float('inf'):
    ans = -1
print(ans)