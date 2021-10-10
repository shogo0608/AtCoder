MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

upper_limit = max(B)
dp = [[0] * (upper_limit + 1) for _ in range(N + 1)]
dp[0] = [1] * (upper_limit + 1)
for i in range(1, N + 1):
    for j in range(upper_limit + 1):
        if j >= A[i-1] and j <= B[i-1]:
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        else:
            dp[i][j] = dp[i][j-1]

print(dp[-1][-1] % MOD)