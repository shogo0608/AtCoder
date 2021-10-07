# 2021/10/07

N = int(input())

name = ""
while N > 0:
    mod26 = (N - 1) % 26
    name = chr(97 + mod26) + name
    N = (N - 1) // 26

print(name)