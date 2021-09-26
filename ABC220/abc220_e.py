MOD = 998244353

N, D = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if i == 1 and D < N:
        ans += 2 ** D
    else:
        if D + i.bit_length() - 1 < N:
            ans += 2 ** D
        
