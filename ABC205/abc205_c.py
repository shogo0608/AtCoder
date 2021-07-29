# 2021/07/29

A, B, C = map(int, input().split())

if A >= 0 and B >= 0:
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')
elif A >= 0:
    if C % 2 == 1:
        print('>')
    else:
        if A > -B:
            print('>')
        elif A < -B:
            print('<')
        else:
            print('=')
elif B >= 0:
    if C % 2 == 1:
        print('<')
    else:
        if -A > B:
            print('>')
        elif -A < B:
            print('<')
        else:
            print('=')
else:
    if C % 2 == 0:
        A *= -1
        B *= -1
    if A > B:
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')