# 2021/10/08

X, N = map(int, input().split())
p = set(map(int, input().split()))

lower = X
while True:
    if lower not in p:
        break
    lower -= 1
upper = X + 1
while True:
    if upper not in p:
        break
    upper += 1
if X - lower < upper - X:
    ans = lower
elif X - lower > upper - X:
    ans = upper
else:
    ans = min(lower, upper)

print(ans)