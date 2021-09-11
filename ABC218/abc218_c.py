N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S_set_h = list(map(set, S))
T_set_h = list(map(set, T))
S_set_v = list(map(set, zip(S)))
T_set_v = list(map(set, zip(T)))

top_S = 0
bottom_S = N-1
left_S = 0
right_S = N-1
while S_set_h[top_S] == set(["."]):
    top_S += 1
while S_set_h[bottom_S] == set(["."]):
    bottom_S -= 1
while S_set_v[left_S] == set(["."]):
    left_S += 1
while S_set_v[right_S] == set(["."]):
    right_S -= 1
top_T = 0
bottom_T = N-1
left_T = 0
right_T = N-1
while T_set_h[top_T] == set(["."]):
    top_T += 1
while T_set_h[bottom_T] == set(["."]):
    bottom_T -= 1
while T_set_v[left_T] == set(["."]):
    left_T += 1
while T_set_v[right_T] == set(["."]):
    right_T -= 1

flag1 = False
flag2 = False
flag3 = False
flag4 = False
if (bottom_S - top_S) == (bottom_T - top_T) and (right_S - left_S) == (right_T - left_T):
    flag1 = True
    flag2 = True
    for i in range(right_S - left_S + 1):
        for j in range(bottom_S - top_S + 1):
            if S[top_S+j][left_S+i] != S[top_T+j][left_T+i]:
                flag1 = False
            if S[bottom_S-j][right_S-i] != S[top_T+j][left_T+i]:
                flag2 = False
if (bottom_S - top_S) == (right_T - left_T) and (right_S - left_S) == (bottom_T - top_T):
    flag3 = True
    flag4 = True
    for i in range(right_S - left_S + 1):
        for j in range(bottom_S - top_S + 1):
            if S[top_S+j][right_S-i] != S[top_T+j][left_T+i]:
                flag3 = False
            if S[bottom_S-j][left_S+i] != S[top_T+j][left_T+i]:
                flag4 = False

print("Yes" if flag1 or flag2 or flag3 or flag4 else "No")