# 2021/08/05

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = min(B) - max(A) + 1
if ans < 0:
    ans = 0

print(ans)