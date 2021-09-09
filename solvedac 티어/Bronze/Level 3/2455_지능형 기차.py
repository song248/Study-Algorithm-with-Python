y = []
for _ in range(4):
    a, b = map(int, input().split())
    if len(y) == 0:
        y.append(b-a)
    else:
        y.append(y[-1]+b-a)
print(max(y))