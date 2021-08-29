# 2021/08/29

from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

S_set = set(S)
cnt_dict = defaultdict(int)
for s in S_set:
    if s[0] == '!':
        cnt_dict[s[1:]] += 1
    else:
        cnt_dict[s] += 1
ans = 'satisfiable'
for k, v in cnt_dict.items():
    if v == 2:
        ans = k
        break

print(ans)
    