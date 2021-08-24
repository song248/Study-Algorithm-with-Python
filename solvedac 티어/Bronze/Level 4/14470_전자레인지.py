a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    print(a*(-1)*c + d + b*e)
elif a > 0:
    print((b-a)*e)
else:
    print(d + (b-a)*e)