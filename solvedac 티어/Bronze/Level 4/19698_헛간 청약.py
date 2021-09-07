n, w, h, l = map(int, input().split())
m = (w//l)*(h//l)
if n < m:    print(n)
else:    print(m)