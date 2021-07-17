from collections import defaultdict

def main():
    N, K = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    
    answer = 0
    now = 0
    c_dict = defaultdict(int)
    for i in range(N):
        c_dict[C[i]] += 1
        if c_dict[C[i]] == 1:
            now += 1
        if i >= K:
            c_dict[C[i-K]] -= 1
            if c_dict[C[i-K]] == 0:
                now -= 1
        answer = max(answer, now)

    print(answer)


if __name__ == '__main__':
    main()