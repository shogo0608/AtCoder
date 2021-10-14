# 2021/10/14

N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = float('inf')
for bit in range(2 ** N):
    mask = [int(b) for b in bin(bit)[2:].zfill(N)]
    C_sum = 0
    A_sum = [0] * M
    for i in range(N):
        if mask[i]:
            C_sum += C[i]
            for j in range(M):
                A_sum[j] += A[i][j]
    if all([a >= X for a in A_sum]):
        ans = min(ans, C_sum)

print(ans if ans != float('inf') else -1)