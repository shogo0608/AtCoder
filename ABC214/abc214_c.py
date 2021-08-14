N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
t_min = [float('inf')] * N

t_min[0] = T[0]
t = 0
for i in range(N):
    t += S[N-1-i]
    t_min[0] = min(t_min[0], T[N-1-i] + t)

for i in range(1, N):
    t_min[i] = min(T[i], t_min[i-1] + S[i-1])

for t in t_min:
    print(t)