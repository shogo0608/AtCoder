# 2021/08/27

S = list(input())

o_set = {idx for idx, val in enumerate(S) if val == 'o'}
x_set = {idx for idx, val in enumerate(S) if val == 'x'}
flag = True
ans = 0
for i in range(10**4):
    pw_set = set(map(int, str(i).zfill(4)))
    flag = True
    if pw_set & o_set != o_set:
        flag = False
    if pw_set & x_set != set():
        flag = False
    if flag:
        ans += 1

print(ans)