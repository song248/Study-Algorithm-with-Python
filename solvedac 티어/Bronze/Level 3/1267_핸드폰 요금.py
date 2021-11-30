n = int(input())
tt = list(map(int, input().split()))

y, m =  0, 0
for t in tt:
    y += (t//30+1) * 10
    m += (t//60+1) * 15
if y < m:
    print('Y {}'.format(y))
elif y > m:
    print('M {}'.format(m))
else:
    print('Y', 'M', y)