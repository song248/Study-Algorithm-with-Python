rest = 0
for _ in range(int(input())):
    s, a = map(int, input().split())
    rest += a%s
print(rest)