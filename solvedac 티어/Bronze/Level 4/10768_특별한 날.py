m = int(input())
d = int(input())

if m < 2:
    print("Before")
else:
    if m == 2:
        if d < 18:
            print("Before")
        elif d == 18:
            print("Special")
        else:
            print('After')
    else:
        print('After')