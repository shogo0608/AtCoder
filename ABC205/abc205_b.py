# 2021/07/28

N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
if sorted_A[0] == 1 and sorted_A[N-1] == N and len(set(A)) == N:
    print('Yes')
else:
    print('No')