def main():
    # 入力
    A, B = [int(i) for i in input().split()]

    # 処理
    total_kcal = A * B / 100

    # 出力
    print(total_kcal)


if __name__ == '__main__':
    main()