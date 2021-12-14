A = list(map(int, input().split()))
B = list(map(int, input().split()))
a, b = 0, 0
state = -1
for i in range(len(A)):
    if A[i] > B[i]:    
        a += 3
        state = 1
    elif A[i] < B[i]:    
        b += 3
        state = 0
    else:
        a += 1
        b += 1
print(a, b)
if a > b:    print('A')
elif a < b:    print('B')
else:    
    if state == 1:
        print('A')
    elif state == 0:
        print('B')
    else:
        print('D')