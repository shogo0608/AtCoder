def a_win_b(a, b, j):
    if hands[a][j] == 'G' and hands[b][j] == 'C':
        return 1
    elif hands[a][j] == 'C' and hands[b][j] == 'P':
        return 1
    elif hands[a][j] == 'P' and hands[b][j] == 'G':
        return 1
    else:
        return 0

N, M = map(int, input().split())
hands = []
for _ in range(2*N):
    hands.append([hand for hand in input()])

win = [[i, 0] for i in range(2 * N)]
for j in range(M):
    for k in range(N):
        if a_win_b(win[2 * k][0], win[2 * k + 1][0], j):
            win[2 * k][1] += 1
        elif a_win_b(win[2 * k + 1][0], win[2 * k][0], j):
            win[2 * k + 1][1] += 1
    win.sort()
    win.sort(key=lambda x: x[1], reverse=True)

for i, _ in win:
    print(i+1)