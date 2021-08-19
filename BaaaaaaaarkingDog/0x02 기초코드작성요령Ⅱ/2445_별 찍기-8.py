n = int(input())
for i in range(n, 0, -1):
    print('*'*(n-i+1)+' '*(i-1)+' '*(i-1)+'*'*(n-i+1))
for i in range(n-1, 0, -1):
    print('*'*i+' '*(n-i)+' '*(n-i)+'*'*i)