def main():
    N, K = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]

    max = 0
    flag = False
    for i in range(N-K+1):
        if flag and num < max:
            flag = False
            continue
        flag = True
        num = len(set(C[i:i+K]))
        if num > max:
            max = num
        if max == K:
            break

    print(max)


if __name__ == '__main__':
    main()