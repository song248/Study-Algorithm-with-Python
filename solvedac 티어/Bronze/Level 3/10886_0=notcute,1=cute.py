zz, oo = 0, 0
for _ in range(int(input())):
    s = int(input())
    if s == 1:  oo += 1
    else:   zz += 1
if oo < zz: print('Junhee is not cute!')
else:   print("Junhee is cute!")