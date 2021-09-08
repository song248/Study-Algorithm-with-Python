for _ in range(int(input())):
    h, w, n = map(int, input().split())
    y, x = n%h, n//h+1
    if y == 0:    y, x = h, x-1
    if x < 10:    print(str(y)+'0'+str(x))
    else:    print(str(y)+str(x))