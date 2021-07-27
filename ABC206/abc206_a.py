from math import floor

N = int(input())

price = floor(1.08*N)

if price < 206:
    print('Yay!')
elif price == 206:
    print('so-so')
else:
    print(':(')