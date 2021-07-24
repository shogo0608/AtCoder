def f(n, m, dp, K):
    if n == 0:
        return 0
    if m == 0:
        return n ** K
    if (n, m) in dp:
        return dp[(n, m)]
    
    dp[(n, m)] = f(n-1, m, dp, K) + f(n, m-1, dp, K)
    return dp[(n, m)]


N, M, K = map(int, input().split())

print(f(N, M, {}, K) % (10**9+7))