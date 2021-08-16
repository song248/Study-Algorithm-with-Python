n = int(input())
dd = []
for _ in range(n):
    key, value = input().split()
    dd.append((key, int(value)))

dd.sort()
# dd = sorted(dd, key=lambda score: score[1])

for d in dd:
    print(d[0], end = ' ')