n = int(input())
F = [0,1]
if n == 0:    print(0)
elif n == 1:    print(1)
else:
    for i in range(2, n+1):
        F.append(F[i-2]+F[i-1])
    print(F[n])