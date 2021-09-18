# 2021/09/16

N, M, T = map(int, input().split())
cafe = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(M)] + [(T, T)]

off_flag = False
battery = N
for i in range(M+1):
    battery -= cafe[i+1][0] - cafe[i][1]
    if battery <= 0:
        off_flag = True
    battery += cafe[i+1][1] - cafe[i+1][0]
    if battery > N:
        battery = N

print("No" if off_flag else "Yes")