fb = list(map(int, input().split()))
sb = list(map(int, input().split()))

print(min(fb[0]+sb[1], fb[1]+sb[0]))