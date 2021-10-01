n = int(input())
for i in range(1, n+1):
    a = ' '*(n-i)
    b = '*'
    if i == 1:
        b = '*'
    elif i == n:
        b = '*'*(n*2-1)
    else:
        b += (' '*((i-1)*2-1)+'*')
    print(a+b)