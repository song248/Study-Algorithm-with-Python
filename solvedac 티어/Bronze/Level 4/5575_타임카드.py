for _ in range(3):
    a = list(map(int, input().split()))
    if a[5] - a[2] < 0:
        a[5] += 60
        a[4] -= 1
    s = a[5] - a[2]

    if a[4] - a[1] < 0:
        a[4] += 60
        a[3] -= 1
    m = a[4] - a[1]
    print(a[3]-a[0], m, s)