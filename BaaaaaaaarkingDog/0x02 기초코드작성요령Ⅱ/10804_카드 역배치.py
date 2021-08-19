card = [x for x in range(1, 21)]
for i in range(10):
    a, b = map(int, input().split())
    card[a-1:b] = reversed(card[a-1:b])
for i in card:
    print(i, end=' ') 
