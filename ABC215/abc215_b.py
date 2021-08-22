# 2021/08/22

N = int(input())

k = 0
while 2 ** k <= N:
    k += 1
k -= 1

print(k)