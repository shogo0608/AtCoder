N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

tl = [0]
tr = [0]
dist = [0]
for i in range(N):
    tl.append(tl[i] + A[i] / B[i])
    tr.append(tr[i] + A[N-i-1] / B[N-i-1])
    dist.append(dist[i] + A[i])

for i in range(N):
    
    print(dist[i] + (A[i] + (tr[i+1] - tl[i]) * B[i]) / 2)