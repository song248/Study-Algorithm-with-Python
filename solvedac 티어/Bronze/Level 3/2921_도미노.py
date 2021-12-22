n = int(input())
ans = 0
for i in range(0, n+1):
    for j in range(i, n+1):
        ans += i+j
print(ans)

n = int(input())
total = 0
for i in range(1, n+2):
    total += i
print(total*n)