# 2021/09/27

MOD = 10**9 + 7

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans += A[i] * A[j]

print(ans % MOD)