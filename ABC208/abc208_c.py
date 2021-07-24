N, K = map(int, input().split())
A = list(map(int, input().split()))

base = K // N
K -= base * N
candies = {}

for nat_id in A:
    candies[nat_id] = base

for nat_id in sorted(candies.keys()):
    if K < 1:
        break
    candies[nat_id] += 1
    K -= 1

for nat_id in A:
    print(candies[nat_id])
