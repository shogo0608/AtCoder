import heapq

Q = int(input())

bag = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(bag, query[1])
    elif query[0] == 2:
        bag = [i + query[1] for i in bag]
    else:
        print(heapq.heappop(bag))