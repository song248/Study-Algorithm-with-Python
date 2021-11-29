for _ in range(int(input())):
    a = a = bin(int(input()))[2:][::-1]
    for i in range(len(a)):
        if a[i] == '1':
            print(i, end=' ')