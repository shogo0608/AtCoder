L, Q = map(int, input().split())
cutted = 0
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        cutted += (1 << (x-1))
    else:
        r = (cutted % (1 << (x-1))).bit_length()
        tmp = (cutted >> x)
        l = (tmp & -tmp).bit_length()
        print(l - r + x if l != 0 else L - r)