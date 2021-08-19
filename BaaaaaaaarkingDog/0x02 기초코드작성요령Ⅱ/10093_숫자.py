a, b = map(int, input().split())
aa = min(a, b)
bb = max(a, b)
if aa == bb: n = 0
else: n = bb-aa-1
print(n)
for i in range(aa+1, bb): print(i, end = ' ')