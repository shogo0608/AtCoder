# 2021/10/05

H, W, K = map(int, input().split())
C = []
for _ in range(H):
    C.append([0 if i=='.' else 1 for i in input()])

ans = 0
# 赤く塗りつぶす行と列をそれぞれbit全探索
for bit_i in range(2**H):
    for bit_j in range(2**W):
        mask_i = bin(bit_i)[2:].zfill(H)
        mask_j = bin(bit_j)[2:].zfill(W)
        cnt = 0
        for i in range(H):
            if mask_i[i] == '1':
                continue
            for j in range(W):
                if mask_j[j] == '1':
                    continue
                if C[i][j]:
                    cnt += 1
        if cnt == K:
            ans += 1

print(ans)