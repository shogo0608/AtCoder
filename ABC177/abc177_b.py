# 2021/10/03

S = input()
T = input()

S_length = len(S)
T_length = len(T)
ans = float('inf')
for i in range(S_length - T_length + 1):
    cnt = len([j for j in range(T_length) if S[i+j] != T[j]])
    ans = min(ans, cnt)

print(ans)