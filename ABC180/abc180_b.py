# 2021/09/29

N = int(input())
X = [abs(i) for i in list(map(int, input().split()))]

e1 = 0
e2 = 0
for x in X:
    e1 += x
    e2 += x ** 2

print(e1)
print(e2 ** 0.5)
print(max(X))