from collections import deque

def solve_graph(s, N, can_move_list):
    # 変数の初期化
    queue = deque(can_move_list[s])
    t = s
    is_arrived = [False] * (N+1)
    is_arrived[s] = True

    while len(queue) != 0:
        t = queue.pop()
        is_arrived[t] = True
        add_city = [u for u in can_move_list[t] if not is_arrived[u]]
        queue.extend(add_city)

    return len([i for i in is_arrived if i])


def main():
    # 入力
    N, M = [int(i) for i in input().split()]
    can_move_list = []
    for i in range(N+1):
        can_move_list.append([i])
    for i in range(M):
        A, B = [int(j) for j in input().split()]
        can_move_list[A].append(B)

    # 処理
    count_pair = 0
    for i in range(1, N+1):
        count_pair += solve_graph(i, N, can_move_list)
    
    # 出力
    print(count_pair)


if __name__ == '__main__':
    main()