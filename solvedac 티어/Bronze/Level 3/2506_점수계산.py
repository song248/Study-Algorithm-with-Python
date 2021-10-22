n = int(input())
sum, result = 0, 0
s = list(map(int, input().split()))
for i in range(n):
    if s[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0
print(result)