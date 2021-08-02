# 2021/08/02

N = int(input())
mountains = []
for _ in range(N):
    s, t = input().split()
    t = int(t)
    mountains.append((s, t))

mountains.sort(key=lambda x: x[1])

print(mountains[-2][0])