N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
i, j = 0, 0
ans = 10 ** 9
while i < N and j < M:
    if A[i] == B[j]:
        ans = 0
        break
    if abs(A[i] - B[j]) < ans:
        ans = abs(A[i] - B[j])
    if i == N-1:
        j += 1
    elif j == M-1:
        i += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1

print(ans)