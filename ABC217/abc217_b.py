S = [input() for _ in range(3)]

contests = set(["ABC", "ARC", "AGC", "AHC"])
print(*(contests - set(S)))