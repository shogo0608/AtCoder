# 2021/08/05

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if (A[j] - A[i]) % 200 == 0:
            ans += 1

print(ans)