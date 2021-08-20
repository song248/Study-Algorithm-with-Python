for _ in range(int(input())):
    a, b = map(str, input().split())
    a, b = sorted(a), sorted(b)
    if a == b:  print("Possible")
    else:   print("Impossible")