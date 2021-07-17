def main():
    N = int(input())
    S = input()

    bad_index = S.find("1")
    if bad_index % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == '__main__':
    main()