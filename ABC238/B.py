# 2022/02/10

N = int(input())
A = list(map(int, input().split()))

cut_degrees = [0]
for i in range(N):
    degree = (cut_degrees[i] + A[i]) % 360
    cut_degrees.append(degree)
cut_degrees.append(360)
cut_degrees.sort()
max_degree = 0
for i in range(N+1):
    max_degree = max(max_degree, cut_degrees[i+1] - cut_degrees[i])

print(max_degree)
