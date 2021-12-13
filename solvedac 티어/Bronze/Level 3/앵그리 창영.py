n, w, h = map(int, input().split())
p = (w**2 + h**2)**(1/2)
for _ in range(n):
    s = int(input())
    if s <= max(w, h, p):
        print('DA')
    else:
        print('NE')