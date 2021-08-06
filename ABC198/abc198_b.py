# 2021/08/06

N = int(input())

N_str = str(N)
zeros = 0
for i in reversed(range(len(N_str))):
    if N_str[i] == "0":
        zeros += 1
    else:
        break
N_str = "0" * zeros + N_str
flag = True
for i in range(len(N_str)//2):
    if N_str[i] != N_str[-1 * i - 1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")