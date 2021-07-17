def main():
    # 入力
    x, y = [int(i) for i in input().split()]

    # 処理と出力
    if x == y:
        print(x)
    else:
        z = [i for i in range(3) if i not in [x, y]]
        print(*z)


if __name__ == '__main__':
    main()