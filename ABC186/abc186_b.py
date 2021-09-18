# 2021/09/14

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_blocks = float('inf')
for blocks in A:
    min_blocks = min(min_blocks, min(blocks))
ans = 0
for blocks in A:
    for block in blocks:
        ans += block - min_blocks

print(ans)