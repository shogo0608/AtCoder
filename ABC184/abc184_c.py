# 2021/09/10

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

two_flag = False
for r in range(4):
    for c in range(4-r):
        two_flag = two_flag or r1 + c1 == (r2 - r) + (c2 - c) or\
               r1 + c1 == (r2 + r) + (c2 + c) or\
               r1 - c1 == (r2 - r) - (c2 - c) or\
               r1 - c1 == (r2 + r) - (c2 + c)
ans = -1
if r1 == r2 and c1 == c2:
    ans = 0
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    ans = 1
elif abs(r1 - r2) + abs(c1 - c2) <= 6 or (r2 - r1 + c2 - c1) % 2 == 0 or two_flag:
    ans = 2
else:
    ans = 3

print(ans)