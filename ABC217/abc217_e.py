from collections import deque

Q = int(input())
A = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A.append(query[1])
    elif query[0] == 2:
        print(A.popleft())
    else:
        A = deque(sorted(A))