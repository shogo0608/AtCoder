# 2021/08/18

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

row_sum = []
for h in range(H):
    row_sum.append(sum(A[h]))
col_sum = []
for c_list in zip(*A):
    col_sum.append(sum(c_list))
ans = [[] for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i].append(row_sum[i] + col_sum[j] - A[i][j])

for i in range(H):
    print(*ans[i])