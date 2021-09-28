# 2021/09/28

N = int(input())
A = list(map(int, input().split()))

max_height = 1
ans = 0
for a in A:
    if a >= max_height:
        max_height = a
    else:
        ans += max_height - a

print(ans)