# 2021/08/07

H, W, X, Y = map(int, input().split())
S = [[] for _ in range(H + 2)]
S[0] = [1] * (W + 2)
for i in range(1, H+1):
    s = input()
    S[i].append(1)
    for c in s:
        if c == '.':
            S[i].append(0)
        else:
            S[i].append(1)
    S[i].append(1)
S[H+1] = [1] * (W + 2)


ans = 1
for c in S[X-1::-1]:
    if c[Y]:
        break
    else:
        ans += 1
for c in S[X+1:]:
    if c[Y]:
        break
    else:
        ans += 1
for c in S[X][Y-1::-1]:
    if c:
        break
    else:
        ans += 1
for c in S[X][Y+1:]:
    if c:
        break
    else:
        ans += 1

print(ans)