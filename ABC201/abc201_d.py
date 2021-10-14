# 2021/10/14

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append([1 if c=='+' else 0 for c in input()])

opt = [[0] * W for _ in range(H)]
for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if i == H-1 and j == W-1:
            opt[i][j] == 0
        elif i == H-1:
            if (i + j) % 2 == 0:
                opt[i][j] = opt[i][j+1] + A[i][j+1]
            else:
                opt[i][j] = opt[i][j+1] - A[i][j+1]
        elif j == W-1:
            if (i + j) % 2 == 0:
                opt[i][j] = opt[i+1][j] + A[i+1][j]
            else:
                opt[i][j] = opt[i+1][j] - A[i+1][j]
        elif (i + j) % 2 == 0:
            opt[i][j] = max(opt[i][j+1] + A[i][j+1], opt[i+1][j] + A[i+1][j])
        else:
            opt[i][j] = min(opt[i][j+1] + A[i][j+1], opt[i+1][j] - A[i+1][j])

if opt[0][0] > 0:
    print("Takahashi")
elif opt[0][0] < 0:
    print("Aoki")
else:
    print("Draw")