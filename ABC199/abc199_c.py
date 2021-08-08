# 2021/08/08

N = int(input())
S = input()
Q = int(input())

order = list(range(2*N))
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        order[A-1], order[B-1] = order[B-1], order[A-1]
    else:
        order[:N], order[N:] = order[N:], order[:N]

for o in order:
    print(S[o], end="")