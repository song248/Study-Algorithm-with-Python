n = int(input())
for i in range(n, 0, -1):
    print(' '*(i-1)+'*'*(n-i+1)+'*'*(n-i))
for i in range(n-1, 0, -1):
    print(' '*(n-i)+'*'*i+'*'*(i-1))