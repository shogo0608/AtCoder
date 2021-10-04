# 2021/10/04

K = int(input())

a = 7 % K
s = set()
for i in range(1, K):
    if a == 0:
        print(i)
        break
    if a in s:
        print(-1)
        break
    s.add(a)
    a = (10 * a + 7) % K