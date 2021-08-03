# 2021/08/03

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

length = [A[0]]
for i in range(1, N):
    length.append(A[i]-A[i-1])
length.append(L-A[N-1])

