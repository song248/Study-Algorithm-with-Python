croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for c in croa:
    s = s.replace(c, 'A')
print(len(s))