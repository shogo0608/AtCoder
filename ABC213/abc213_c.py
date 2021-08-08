H, W, N = map(int, input().split())
cards = {}
rows = set()
cols = set()
for i in range(1, N+1):
    a, b = map(int, input().split())
    cards[i] = (a, b)
    rows.add(a)
    cols.add(b)

for i in range(1, N+1):
    a, b = cards[i]
    new_a = len(list(filter(lambda x: x < a, rows))) + 1
    new_b = len(list(filter(lambda x: x < b, cols))) + 1
    print(new_a, new_b)