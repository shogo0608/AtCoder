# 2021/09/21

sx, sy, gx, gy = map(int, input().split())

if sx == gx:
    ans = sx
else:
    ans = (sy * gx + gy * sx) / (gy + sy)

print(ans)