def main():
    A, B = map(int, input().split())

    answer = 0
    if A < B:
        answer = B - A + 1

    print(answer)

if __name__ == '__main__':
    main()