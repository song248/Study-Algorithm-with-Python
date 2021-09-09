for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        if b%4 == 0:
            print(str(a**4)[-1])
        else:
            print(str(a**(b%4))[-1])
    elif a == 4 or a == 9:
        if b%2 == 1:
            print(a)
        else:
            print((a**2)%10)