# 2021/08/21

N, K = map(int, input().split())

def g1(N):
    return int("".join(sorted(str(N), reverse=True)))

def g2(N):
    return int("".join(sorted(str(N))))

def f(N):
    return g1(N) - g2(N)

a = N
for i in range(1, K+1):
    a = f(a)

print(a)
