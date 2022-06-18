# 2022/06/19

N = int(input())
next_nodes_cnt = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    next_nodes_cnt[a-1] += 1
    next_nodes_cnt[b-1] += 1
    
if any([n == N-1 for n in next_nodes_cnt]):
    print("Yes")
else:
    print("No")