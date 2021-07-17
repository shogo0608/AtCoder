def main():
    N, A, X, Y = [int(i) for i in input().split()]

    if N > A:
        total_price = X * A + Y * (N-A)
    else:
        total_price = X * N
    
    print(total_price)


if __name__ == '__main__':
    main()