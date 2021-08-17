# 2021/08/17

N = int(input())

i = 1
while int(str(i) + str(i)) <= N:
    i += 1

print(i-1)