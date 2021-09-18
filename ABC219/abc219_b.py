S = [input() for _ in range(3)]
T = [int(c) for c in input()]

print("".join([S[i-1] for i in T]))