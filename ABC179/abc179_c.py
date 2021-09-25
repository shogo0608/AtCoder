# 2021/09/25

N = int(input())

ans = 0
for A in range(1, N):
    ans += N // A
    if N % A == 0:
        ans -= 1

print(ans)