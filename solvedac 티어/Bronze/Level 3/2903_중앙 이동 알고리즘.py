n = [2]
f = 1
for i in range(1, 16):
    n.append(n[-1] + f)
    f *= 2
print(n[int(input())]**2)