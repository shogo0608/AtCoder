N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

time = [0]
for i in range(N):
    time.append(time[i] + A[i] / B[i])
conflict_time = time[-1] / 2
ans = 0
for i in range(N):
    if time[i + 1] < conflict_time:
        ans += A[i]
    elif time[i + 1] == conflict_time:
        ans += A[i]
        break
    else:
        ans += B[i] * (conflict_time - time[i])
        break

print(ans)