hap, cha = map(int, input().split())
a = (hap+cha)//2
b = hap - a
if hap < cha or (hap-cha)%2 != 0:
    print(-1)
else:   print(max(a,b), min(a,b))