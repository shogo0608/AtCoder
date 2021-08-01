# 2021/08/01

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort(key=lambda x: B[x-1])

ans = 0
i, j = 0, 0
while i < N and j < N:
    if A[i] == B[C[j]-1]:
        ans += 1
        for k in A[i+1:]:
            if k == A[i]:
                ans += 1
            else:
                break
    if i == N - 1:
        j += 1
    elif j == N - 1:
        k = A[i]
        while i < N and k == A[i]:
            i += 1
    elif A[i] < B[C[j]-1]:
        k = A[i]
        while i < N and k == A[i]:
            i += 1
    else:
        j += 1

print(ans)