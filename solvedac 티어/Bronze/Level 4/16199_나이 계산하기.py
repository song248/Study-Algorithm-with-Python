y, m, d = map(int, input().split())
ny, nm, nd = map(int, input().split())

if nm < m:  print(ny-y-1)
elif nm == m:
    if nd < d:  print(ny-y-1)
    else: print(ny-y)
else:    print(ny-y)
print(ny - y+1)
print(ny - y)