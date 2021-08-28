# 2021/08/28

N = int(input())
S = list(input())
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

swap_flag = -1
for t, a, b in queries:
    a, b = a-1, b-1
    if t == 1:
        if swap_flag == 1:
            if a < N:
                a += N
            else:
                a -= N
            if b < N:
                b += N
            else:
                b -= N
        S[a], S[b] = S[b], S[a]
    if t == 2:
        swap_flag *= -1
if swap_flag == 1:
    S[:N], S[N:] = S[N:], S[:N]

print(*S, sep='')