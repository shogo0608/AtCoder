N = int(input())
A = list(map(int, input().split()))
X = int(input())

cusum = [-1] * N
cusum[0] = A[0]
for i in range(1, N):
    cusum[i] = cusum[i-1] + A[i]
block = X // cusum[-1]
X = X - (block * cusum[-1])
ans = 0
for i in range(N):
    if cusum[i] > X:
        ans = i + 1
        break
print(ans + (block * N))