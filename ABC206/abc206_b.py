N = int(input())

i = 0
stored = 0
while True:
    i += 1
    stored += i
    if stored >= N:
        print(i)
        break
