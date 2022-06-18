# 2022/06/19

S = input()

if len(set(S)) == 3:
    print(6)
elif len(set(S)) == 2:
    print(3)
else:
    print(1)