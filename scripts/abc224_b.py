# 2022/02/04
H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

flag = False
for i1 in range(H):
    for j1 in range(W):
        for i2 in range(i1+1, H):
            for j2 in range(j1+1, W):
                if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                    flag = True

print("Yes" if not flag else "No")

