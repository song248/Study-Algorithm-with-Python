n = int(input())
for i in range(1, n+1):
    a = ' '*(n-i)
    if i == 1:
        b = '*'
    else:
        b += ' *'
    print(a+b)