# 2021/09/24

N = int(input())
A = list(map(int, input().split()))

max_gcd = 0
for i in range(2, max(A)+1):
    gcd = len([j for j in A if j % i == 0])
    if gcd > max_gcd:
        max_gcd = gcd
        ans = i

print(ans)