A, B = map(int, input().split())

if B < A:
    print('No')
elif B > A * 6:
    print('No')
else:
    print('Yes')