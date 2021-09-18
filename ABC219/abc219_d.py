from itertools import combinations

N = int(input())
X, Y = map(int, input().split())
box = [tuple(map(int, input().split())) for _ in range(N)]

A, B = zip(*box)
if (sum(A) >= X) and (sum(B) >= Y):
    ans = N
    left = 1
    right = N + 1
    middle = (left + right) // 2
    while left != middle:
        flag = False
        for p in combinations(range(N), middle):
            tmp_A = 0
            tmp_B = 0
            for idx in p:
                tmp_A += A[idx]
                tmp_B += B[idx]
            if tmp_A >= X and tmp_B >= Y:
                flag = True
        if flag:
            ans = middle
            right = middle
        else:
            left = middle
        middle = (left + right) // 2
    print(ans)
else:
    print(-1)
