N = int(input())
names = [tuple(input().split()) for _ in range(N)]

flag = False
for i in range(N):
  for j in range(i+1, N):
    if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
      flag = True
      
print("Yes" if flag else "No")