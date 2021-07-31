X = list(map(int, input()))

flag = 0

for i in range(3):
    if X[i] != X[i+1]:
        flag = 1

if flag:
    flag = 0
    for i in range(1, 4):
        if (X[0]+i) % 10 != X[i]:
            flag = 1

if flag:
    print("Strong")
else:
    print("Weak")