# 2021/10/11

N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            flag1 = L[i] + L[j] > L[k]
            flag2 = L[j] + L[k] > L[i]
            flag3 = L[k] + L[i] > L[j]
            flag4 = L[i] != L[j]
            flag5 = L[j] != L[k]
            flag6 = L[k] != L[i]
            if flag1 and flag2 and flag3 and flag4 and flag5 and flag6:
                ans += 1

print(ans)