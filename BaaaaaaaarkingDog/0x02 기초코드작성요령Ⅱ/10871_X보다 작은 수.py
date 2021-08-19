n, x = map(int, input().split())
aaa = list(map(int, input().split()))
for i in aaa:
  if i < x:
    print(i, end = ' ')