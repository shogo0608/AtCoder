# 2021/09/27

N = int(input())
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if (B - A) % 2 == 0:
        ans += (A + B) * ((B - A + 1) // 2) + (A + B) // 2
    else:
        ans += (A + B) * ((B - A + 1) // 2)

print(ans)