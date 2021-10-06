# 2021/10/06

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_cusum = [0]
B_cusum = [0]
for i in range(N):
    A_cusum.append(A_cusum[i] + A[i])
for i in range(M):
    B_cusum.append(B_cusum[i] + B[i])
ans = 0
j = M
for i in range(N+1):
    while j >= 0:
        if A_cusum[i] + B_cusum[j] <= K:
            ans = max(ans, i + j)
            break
        else:
            j -= 1

print(ans)