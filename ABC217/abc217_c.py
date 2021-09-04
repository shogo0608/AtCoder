N = int(input())
P = [(q+1, p) for q, p in enumerate(map(int, input().split()))]

P.sort(key=lambda x: x[1])
for q, _ in P:
    print(q, end=" ")
