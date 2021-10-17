S = input()

S_len = len(S)
strings = []
for i in range(S_len):
    strings.append(S[i:] + S[:i])

strings.sort()
print(strings[0], strings[-1], sep="\n")