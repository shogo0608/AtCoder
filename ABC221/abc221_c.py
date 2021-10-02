N = int(input())

dig = [i for i in str(N)]
ans = 0
for bit in range(1, (2 ** len(dig)) - 1):
    list1 = []
    list2 = []
    for i in range(len(dig)):
        if bit % 2 == 1:
            list1.append(dig[i])
        else:
            list2.append(dig[i])
        bit //= 2
    num1 = int("".join(sorted(list1, reverse=True)))
    num2 = int("".join(sorted(list2, reverse=True)))
    ans = max(ans, num1 * num2)

print(ans)