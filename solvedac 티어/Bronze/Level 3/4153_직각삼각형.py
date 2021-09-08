while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:    break
    else:
        m = max(a)
        a.remove(m)
        if a[0]**2 + a[1]**2 == m**2:    print("right")
        else:    print("wrong")