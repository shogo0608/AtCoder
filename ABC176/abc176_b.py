# 2021/10/04

N = int(input())

D = [int(d) for d in str(N)]

print("Yes" if sum(D) % 9 == 0 else "No")