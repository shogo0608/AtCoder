def main():
    # 入力
    N = int(input())
    A = [int(i) for i in input().split()]

    # 処理
    total_nuts = 0
    for num_nuts in A:
        if num_nuts > 10:
            total_nuts += num_nuts - 10

    # 出力
    print(total_nuts)


if __name__ == '__main__':
    main()