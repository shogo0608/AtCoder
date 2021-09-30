# 2021/09/30

X, K, D = map(int, input().split())

X = abs(X)
ans = X
# 往復する回数
left = 0
right = (K // 2) + 1
mid = (left + right) // 2
while left != mid:
    target = X - D * (K - 2 * mid)
    if abs(target) < ans:
        ans = target
    if target > 0:
        right = mid
        mid = (left + right) // 2
    elif target < 0:
        left = mid
        mid = (left + right) // 2
    else:
        left = mid
ans = min(ans, abs(X - D * (K - 2 * mid)))

print(ans)