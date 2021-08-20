n = int(input())
total, pp = 2, 2
for i in range(1, n):
    total += pp
    if i%2 == 0:
        pp += 1
print(total)