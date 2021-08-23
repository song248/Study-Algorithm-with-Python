a, b, c = list(map(int, input().split()))
print(max(int(a/b*c), int(a*b/c)))