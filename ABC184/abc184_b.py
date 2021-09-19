# 2021/09/19

N, X = map(int, input().split())
S = input()

for result in S:
    if result == 'o':
        X += 1
    else:
        if X > 0:
            X -= 1

print(X)