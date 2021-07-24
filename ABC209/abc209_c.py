def main():
    # 入力
    N = int(input())
    C = list(map(int, input().split()))

    answer = 1
    for i in range(N):
        answer *= C[i] - i
    
    print(answer%(10**9+7))

if __name__ == '__main__':
    main()