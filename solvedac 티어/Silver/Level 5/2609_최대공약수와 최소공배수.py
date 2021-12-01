a, b = map(int, input().split())
c = max(a, b)
for i in range(c,0,-1):
    if a%i == 0 and b%i == 0:
        gcd = i
        break
lcm = a*b//gcd
print(gcd)
print(lcm)