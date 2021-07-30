# 2021/07/30

N, K = map(int, input().split())

ans = 0
ans += ((N+1) * N // 2) * 100 * K # 階数
ans += ((K+1) * K // 2) * N       # 部屋番号

print(ans)