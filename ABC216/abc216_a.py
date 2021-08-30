N = input()
X = int(float(N))
Y = int(N[-1])

if Y <= 2:
    print(X, "-", sep="")
elif Y <= 6:
    print(X)
else:
    print(X, "+", sep="")