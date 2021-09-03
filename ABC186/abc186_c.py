# 2021/09/03

N = int(input())

ans = sum(['7' not in str(i) and '7' not in oct(i) for i in range(1, N+1)])

print(ans)