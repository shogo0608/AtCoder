# 2021/08/17

N = int(input())

n_digits = len(str(N))
if n_digits < 4:
    ans = 0
elif n_digits < 7:
    ans = N - 999
elif n_digits < 10:
    ans = 999000 + 2 * (N - 999999)
elif n_digits < 13:
    ans = 999000 + 2 * 999000000 + 3 * (N - 999999999)
else:
    ans = 999000 + 2 * 999000000 + 3 * 999000000000 + 4 * (N - 999999999999)

print(ans)