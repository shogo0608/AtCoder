# 2021/08/21

S = input()

hard_to_read = True
S_len = len(S)
for i in range(0, S_len, 2):
    if S[i].isupper():
        hard_to_read = False
for i in range(1, S_len, 2):
    if S[i].islower():
        hard_to_read = False

if hard_to_read:
    print("Yes")
else:
    print("No")