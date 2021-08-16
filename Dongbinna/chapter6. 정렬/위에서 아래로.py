n = int(input())
iii = [int(input()) for _ in range(n)]
iii.sort(reverse = True)
for i in iii:
    print(i, end = ' ')