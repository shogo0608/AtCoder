N = int(input())
A = list(map(int, input().split()))
 
order = list(range(1, N+1))
order.sort(key=lambda x: A[x-1])
 
print(order[-2])