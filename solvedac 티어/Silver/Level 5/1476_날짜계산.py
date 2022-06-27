e, s, m = map(int, input().split())
y = 1
while True:
    if (e-y)%15 == 0 and (s-y)%28 == 0 and (m-y)%19 == 0:
        break
    y += 1
print(y)