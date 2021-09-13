# 2021/09/13

N = int(input())

digits = [int(i) for i in str(N)]
ans = float('inf')
for i in range(2**len(digits)-1):
    bit = bin(i)[2:].rjust(len(digits), "0")
    if sum([digits[j] for j in range(len(digits)) if bit[j] == "0"]) % 3 == 0:
        ans = min(ans, bin(i).count("1"))

print(-1 if ans == float('inf') else ans)