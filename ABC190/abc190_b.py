# 2021/08/31

N, S, D = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(N)]

flag = False
for x, y in magic:
    if x < S and y > D:
        flag = True

print("Yes" if flag else "No")