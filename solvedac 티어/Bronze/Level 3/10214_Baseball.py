for _ in range(int(input())):
    y, k = 0, 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y == k:
        print('Draw')
    elif y > k:
        print('Yonsei')
    else:
        print('Korea')