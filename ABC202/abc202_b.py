# 2021/08/01

S = input()

ans = ""
for s in S:
    if s in ["0", "1", "8"]:
        ans = s + ans
    elif s == "6":
        ans = "9" + ans
    else:
        ans = "6" + ans

print(ans)