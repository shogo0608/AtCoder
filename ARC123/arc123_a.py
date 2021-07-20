def main():
    A = list(map(int, input().split()))

    answer = 0
    if A[0] + A[2] < 2 * A[1]:
        answer = 2 * A[1] - A[0] - A[2]
    elif A[0] + A[2] > 2 * A[1]:
        if (A[0] + A[2] - 2 * A[1]) % 2 == 0:
            answer = (A[0] + A[2] - 2 * A[1]) // 2
        else:
            answer = (A[0] + A[2] - 2 * A[1]) // 2 + 2
    else:
        answer = 0
    
    print(answer)


if __name__ == '__main__':
    main()