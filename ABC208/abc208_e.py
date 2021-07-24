N, K = map(int, input().split())

answer = 0
for n in range(1, N+1):
    n_digits = list(map(int, str(n)))
    mul = 1
    for dig in n_digits:
        mul *= dig
    if mul <= K:
        answer += 1

print(answer)