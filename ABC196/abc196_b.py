# 2021/08/13

X = input()

if "." in X:
    dot_idx = X.index(".")
    print(X[:dot_idx])
else:
    print(X)
