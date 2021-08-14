n, m, k = map(int, input().split())
index = list(map(int, input().split()))

index.sort(reverse=True)

maaaax = index[0]
neeext = index[1]
total = 0

while m > 0:
    for _ in range(k):
        if m == 0: 
            break
        total += maaaax
        m -= 1
    if m == 0:
        break
    total += neeext
    m -= 1

print(total)