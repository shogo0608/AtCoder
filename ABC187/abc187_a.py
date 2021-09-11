# 2021/09/07

A, B = map(int, input().split())

def S(n: int) -> int:
    return sum(map(int, str(n)))

print(max(S(A), S(B)))
