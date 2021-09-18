X = input()
N = int(input())
S = [input() for _ in range(N)]

convert_table = {}
for i in range(len(X)):
    convert_table[X[i]] = chr(97+i)
converted = []
for i in range(N):
    converted.append(("".join([convert_table[c] for c in S[i]]), i))
converted.sort(key=lambda x: x[0])

for _, idx in converted:
    print(S[idx])