# 2021/09/25
MOD = 10**9 + 7

N = int(input())

ans = 10**N - 9**N - 9**N + 8**N

print(ans % MOD)