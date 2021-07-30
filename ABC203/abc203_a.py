# 2021/07/30

a, b, c = map(int, input().split())

if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(0)