# 2021/08/29

N = int(input())
A = [a for a in enumerate(map(int, input().split()))]

lmax = max(A[:2**(N-1)], key=lambda x: x[1])
rmax = max(A[2**(N-1):], key=lambda x: x[1])

print(min(lmax, rmax, key=lambda x: x[1])[0] + 1)