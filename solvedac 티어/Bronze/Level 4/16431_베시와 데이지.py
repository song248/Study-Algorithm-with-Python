b = list(map(int, input().split()))
d = list(map(int, input().split()))
j = list(map(int, input().split()))

dtoj = abs(j[0]-d[0])+abs(j[1]-d[1])
btoj = max(abs(j[0]-b[0]), abs(j[1]-b[1]))

if dtoj > btoj: print("bessie")
elif dtoj < btoj:   print("daisy")
else:   print("tie")