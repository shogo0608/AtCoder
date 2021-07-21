def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    answer = 0
    for i in range(N):
        if i % 2 == 0:
            answer += A[i]
        else:
            answer += A[i] - 1
        
    if X >= answer:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()