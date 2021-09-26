A, B, C = map(int, input().split())

flag = False
for i in range(A, B+1):
    if i % C == 0 and not flag:
        print(i)
        flag = True

if not flag:
    print(-1)