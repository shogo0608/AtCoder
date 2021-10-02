S = input()
T = input()

if S == T:
    print("Yes")
else:
    idx = [i for i in range(len(S)) if S[i] != T[i]]
    if len(idx) == 2 and idx[0] == idx[1] - 1:
        if S[idx[0]] == T[idx[1]] and S[idx[1]] == T[idx[0]]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
