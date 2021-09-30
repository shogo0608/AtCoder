# 2021/09/30

N = int(input())
doubles_streak = 0
flag = False
for _ in range(N):
    c1, c2 = map(int, input().split())
    if c1 == c2:
        doubles_streak += 1
    else:
        doubles_streak = 0
    if doubles_streak == 3:
        flag = True

print("Yes" if flag else "No")
