# 2021/08/23

N, X = map(int, input().split())
A = [a for a in map(int, input().split()) if a != X]

print(*A)