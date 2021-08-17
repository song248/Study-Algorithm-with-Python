# 브론즈 3이여도 될거 같은데... 
h, m, s = map(int, input().split())
tt = int(input())
s += tt%60
if s >= 60:
    s %= 60
    m += 1
m += tt//60%60
if m >= 60:
    m %= 60
    h += 1
h += tt//3600
if h >= 24:
    h %= 24
print(h, m, s)